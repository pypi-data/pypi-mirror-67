"""Contains helper functions to modify classes that overwrite specific methods."""
import dataclasses
from typing import Type, Dict

from autoconfiguration.exceptions.config_class_errors import ConfigClassAttributeError


class _MISSING_VALUE:
    pass


MISSING_VALUE = _MISSING_VALUE()


def make_singleton(obj: Type):
    """
    Modifies the passed type to ensure that only one instance of the type can be
    created.

    :param obj: The type that should be a singleton
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance") or not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    setattr(obj, "__new__", __new__)


def add_contains_getattribute_getitem_get_methods_to(cls, available_attributes: Dict):
    """
    Adds implementations to the passed instance of a class for the following methods:

    - __contains__: Checks if _sections of the instance contains the passed str
    - __getattribute__: Used to raise an exception if no value was specified for an attribute
    - __getitem__: Returns the value by the passed key of _sections of the instance
    - get: Returns the value by the passed key of _sections of the instance. Has a second parameter for a default value (default: None)

    :param cls: The class to which the methods should be added
    :param available_attributes: A dict containing available attributes of the class
    """
    setattr(cls, "__contains__", lambda self, item: item in available_attributes)
    setattr(cls, "__getitem__", lambda self, item: self.__dict__[item])
    setattr(
        cls,
        "get",
        lambda self, section_name, default_value=None: self[section_name]
        if section_name in self
        else default_value,
    )

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if value == MISSING_VALUE:
            raise ConfigClassAttributeError(item)
        return value

    setattr(cls, "__getattribute__", __getattribute__)


def freeze_class(cls):
    """
    Freezes a class by adding implementations for the following methods:
    - __delattr__: Raises a FrozenInstanceError
    - __setattr__: Raises a FrozenInstanceError

    :param cls: The class that should be frozen
    """

    def __delattr__(self, name):
        raise dataclasses.FrozenInstanceError()

    setattr(cls, "__delattr__", __delattr__)

    def __setattr__(self, name, value):
        raise dataclasses.FrozenInstanceError()

    setattr(cls, "__setattr__", __setattr__)
