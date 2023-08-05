import inspect
from pygraphy.utils import (
    to_snake_case,
    patch_indents
)
from .field import ResolverField, FieldableType


class InterfaceType(FieldableType):

    def __new__(cls, name, bases, attrs):
        cls = super().__new__(cls, name, bases, attrs)
        for name in dir(cls):
            attr = getattr(cls, name)
            field_name = None
            if hasattr(attr, '__is_field__'):
                field_name = to_snake_case(name)
            elif hasattr(attr, '__is_metafield__'):
                field_name = f'_{name}'

            if field_name:
                sign = inspect.signature(attr)
                cls.__fields__[field_name] = ResolverField(
                    name=field_name,
                    _ftype=sign.return_annotation,
                    _params=cls.remove_self(sign.parameters),
                    description=inspect.getdoc(attr),
                    _obj=cls
                )
        return cls

    @staticmethod
    def remove_self(param_dict):
        result = {}
        first_param = True
        for name, param in param_dict.items():
            if first_param:
                first_param = False
                continue
            result[name] = param
        return result

    def __str__(cls):
        return (
            f'{cls.print_description()}'
            + f'interface {cls.__name__} '
            + '{\n'
            + f'{patch_indents(cls.print_field(), indent=1)}'
            + '\n}'
        )


class Interface(metaclass=InterfaceType):
    pass
