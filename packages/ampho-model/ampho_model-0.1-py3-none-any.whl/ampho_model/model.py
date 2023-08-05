"""Ampho Abstract Data Model
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Any
from abc import ABC, abstractmethod


class Model(ABC):
    """Ampho Abstract Data Model
    """

    @abstractmethod
    def get_value(self, field_name: str) -> Any:
        """Get entity field's value
        """

    @abstractmethod
    def set_value(self, field_name: str, value: Any):
        """Set entity field's value
        """

    @abstractmethod
    def add_value(self, field_name: str, value: Any):
        """Add a value to the field
        """

    @abstractmethod
    def remove_value(self, field_name: str, value: Any):
        """Remove a value from the field
        """

    @abstractmethod
    def contains_value(self, field_name: str, value: Any) -> bool:
        """Check whether the field contains a value
        """

    @abstractmethod
    def save(self):
        """Save the entity
        """

    @abstractmethod
    def delete(self):
        """Delete the entity
        """
