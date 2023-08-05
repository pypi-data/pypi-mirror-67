import asyncio
import json
import logging
import contextvars
from typing import TypeVar
from abc import abstractmethod, ABC
from graphql.language import parse
from graphql.language.ast import (
    OperationDefinitionNode,
    OperationType
)
from pygraphy.utils import (
    is_union,
    is_list,
    is_optional,
    patch_indents
)
from pygraphy.encoder import GraphQLEncoder
from pygraphy.exceptions import ValidationError
from pygraphy.context import Context
from .object import ObjectType, Object
from .field import Field, ResolverField
from .union import UnionType
from .input import InputType
from .interface import InterfaceType
from .enum import EnumType


class SchemaType(ObjectType):
    VALID_ROOT_TYPES = {'query', 'mutation', 'subscription'}

    def __new__(cls, name, bases, attrs):
        attrs['registered_type'] = []
        without_dataclass = type.__new__(cls, name, bases, attrs)

        cls = super().__new__(cls, name, bases, attrs)
        cls.validated_type = []
        cls.validate()
        cls.register_fields_type(cls.__fields__.values())

        for parent in cls.__mro__:
            if hasattr(parent, "__fields__"):
                for key, field in parent.__fields__.items():
                    if key not in cls.__fields__:
                        cls.__fields__[key] = field
            if hasattr(parent, "registered_type"):
                existing_type_name = [t.__name__ for t in cls.registered_type]
                for ptype in parent.registered_type:
                    if ptype.__name__ not in existing_type_name:
                        cls.registered_type.append(ptype)

        # Schema does not need to be a dataclass
        without_dataclass.__fields__ = cls.__fields__
        without_dataclass.__description__ = cls.__description__
        without_dataclass.registered_type = cls.registered_type
        return without_dataclass

    def register_fields_type(cls, fields):
        param_return_types = []
        for field in fields:
            param_return_types.append(field.ftype)
            if isinstance(field, ResolverField):
                param_return_types.extend(field.params.values())
        cls.register_types(param_return_types)

    def register_types(cls, types):
        for ptype in types:
            if ptype in cls.validated_type:
                continue
            cls.validated_type.append(ptype)

            if isinstance(ptype, ObjectType):
                cls.registered_type.append(ptype)
                cls.register_fields_type(ptype.__fields__.values())
            elif is_union(ptype) or is_list(ptype):
                cls.register_types(ptype.__args__)
            elif isinstance(ptype, UnionType):
                cls.registered_type.append(ptype)
                cls.register_types(ptype.members)
            elif isinstance(ptype, InputType):
                cls.registered_type.append(ptype)
                cls.register_fields_type(ptype.__fields__.values())
            elif isinstance(ptype, InterfaceType):
                cls.registered_type.append(ptype)
                cls.register_fields_type(ptype.__fields__.values())
                cls.register_types(ptype.__subclasses__())
            elif isinstance(ptype, EnumType):
                cls.registered_type.append(ptype)
            else:
                # Other basic types, do not need be handled
                pass

    def validate(cls):
        for name, field in cls.__fields__.items():
            if name not in cls.VALID_ROOT_TYPES:
                raise ValidationError(
                    f'The valid root type must be {cls.VALID_ROOT_TYPES},'
                    f' rather than {name}'
                )
            if not isinstance(field, Field):
                raise ValidationError(f'{field} is an invalid field type')
            if not is_optional(field.ftype):
                raise ValidationError(
                    f'The return type of root object should be Optional'
                )
            if not isinstance(field.ftype.__args__[0], ObjectType):
                raise ValidationError(
                    f'The typt of root object must be an Object, rather than {field.ftype}'
                )
        ObjectType.validate(cls)

    def __str__(cls):
        string = ''
        for rtype in cls.registered_type:
            string += (str(rtype) + '\n\n')
        schema = (
            f'{cls.print_description()}'
            + f'schema '
            + '{\n'
            + f'{patch_indents(cls.print_field(), indent=1)}'
            + '\n}'
        )
        return string + schema


context: contextvars.ContextVar[Context] = contextvars.ContextVar('context')


class Schema(Object, metaclass=SchemaType):

    OPERATION_MAP = {
        OperationType.QUERY: 'query',
        OperationType.MUTATION: 'mutation',
    }

    @classmethod
    async def execute(cls, query, variables=None, request=None, serialize=False):
        document = parse(query)
        operation_result = {
            'errors': None,
            'data': None
        }
        for definition in document.definitions:
            if not isinstance(definition, OperationDefinitionNode):
                continue

            if definition.operation not in cls.OPERATION_MAP \
               or cls.OPERATION_MAP[definition.operation] not in cls.__fields__:
                operation_result = {
                    'errors': {
                        'message': 'This API does not support this operation'
                    },
                    'data': None
                }
                break
            async for operation_result in cls._execute_operation(
                document,
                definition,
                variables,
                request
            ):
                pass

        if serialize:
            return json.dumps(operation_result, cls=GraphQLEncoder)
        else:
            return operation_result

    @classmethod
    async def _execute_operation(cls, document, definition, variables, request):
        obj = cls.__fields__[
            cls.OPERATION_MAP[definition.operation]
        ].ftype.__args__[0]()
        error_collector = []
        token = context.set(
            Context(
                schema=cls,
                root_ast=document.definitions,
                request=request,
                variables=variables
            )
        )
        try:
            async for obj in await obj._resolve(
                definition.selection_set.selections,
                error_collector
            ):
                return_root = {
                    'errors': error_collector if error_collector else None,
                    'data': dict(obj) if obj else None
                }
                yield return_root
        except Exception as e:
            logging.error(e, exc_info=True)
            error_collector.append(e)
        finally:
            context.reset(token)


class Socket(ABC):

    @abstractmethod
    async def send(self, text: str):
        pass

    @abstractmethod
    async def receive(self) -> str:
        pass

    @abstractmethod
    async def close(self):
        pass


T = TypeVar("T", bound=Socket)


class SubscribableSchema(Schema):
    OPERATION_MAP = {
        OperationType.QUERY: 'query',
        OperationType.MUTATION: 'mutation',
        OperationType.SUBSCRIPTION: 'subscription'
    }

    @classmethod
    async def execute(cls, socket: T):
        subscription_router = {}

        while True:
            try:
                message = await socket.receive()
            except Exception:
                await socket.close()
                return
            try:
                data = json.loads(message)
            except Exception as e:
                logging.error(e, exc_info=True)
                await cls.send_connection_error(socket, e)
                continue

            query_type, payload = data['type'], data.get('payload')
            if query_type == 'connection_init':
                asyncio.ensure_future(cls.start_ack_loop(socket))
            elif query_type == 'start':
                id = data['id']
                variables, query = payload['variables'], payload['query']
                task = asyncio.ensure_future(cls.subscribe(socket, id, query, variables))
                subscription_router[id] = task
            elif query_type == 'stop':
                id = data['id']
                task = subscription_router.get(id)
                if task:
                    task.cancel()
                    del subscription_router[id]
            else:
                await cls.send_connection_error(socket, f'Unsupported message type {repr(query_type)}')
                return

    @classmethod
    async def subscribe(cls, socket, id, query, variables):
        document = parse(query)
        for definition in document.definitions:
            if not isinstance(definition, OperationDefinitionNode):
                continue

            if cls.OPERATION_MAP[definition.operation] not in cls.__fields__:
                await cls.send_error(socket, id, 'This API does not support this operation')
                break

            async for operation_result in cls._execute_operation(
                document, definition, variables, socket
            ):
                try:
                    await socket.send(
                        json.dumps({
                                'type': 'data',
                                'id': id,
                                'payload': operation_result
                            },
                            cls=GraphQLEncoder
                        )
                    )
                except Exception as e:
                    logging.error(e, exc_info=True)
                    raise
            try:
                await socket.send(
                    json.dumps({
                            'type': 'complete',
                            'id': id,
                        },
                        cls=GraphQLEncoder
                    )
                )
            except Exception as e:
                logging.error(e, exc_info=True)
                raise
            break

    @staticmethod
    async def send_error(socket, id, e):
        try:
            await socket.send(
                json.dumps({
                        'type': 'error',
                        'id': id,
                        'payload': {
                            'errors': {
                                'message': e
                            },
                            'data': None
                        }
                    },
                    cls=GraphQLEncoder
                )
            )
        except Exception as e:
            logging.error(e, exc_info=True)
            raise

    @staticmethod
    async def send_connection_error(socket, e):
        try:
            await socket.send(
                json.dumps({
                        'type': 'connection_error',
                        'payload': {
                            'errors': {
                                'message': e
                            },
                            'data': None
                        }
                    },
                    cls=GraphQLEncoder
                )
            )
        except Exception as e:
            logging.error(e, exc_info=True)
            raise

    @staticmethod
    async def start_ack_loop(socket, sleep=20):
        try:
            await socket.send(
                json.dumps({
                    'type': 'connection_ack'
                })
            )
        except RuntimeError:
            # socket closed
            return
        while True:
            try:
                await socket.send(
                    json.dumps({
                        'type': 'ka'
                    })
                )
            except RuntimeError:
                # socket closed
                return
            await asyncio.sleep(sleep)
