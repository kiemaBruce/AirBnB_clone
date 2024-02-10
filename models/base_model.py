#!/usr/bin/python3
"""Contains BaseModel class
"""


from datetime import datetime
import uuid


class BaseModel:
    """Defines common attributes/methods for other classes."""

    def __init__(self):
        """Initializes instance attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict with all keys/values of __dict__ of the instance."""
        full_dict = self.__dict__.copy()
        # 		updated_at_str = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        full_dict["created_at"] = self.created_at.isoformat()
        full_dict["updated_at"] = self.updated_at.isoformat()
        full_dict["__class__"] = self.__class__.__name__
        return full_dict

    def __str__(self):
        """Returns human-readable string representation of instance."""
        class_name = self.__class__.__name__
        r_str = f"[{class_name}] ({self.id}) {self.__dict__}"
        return r_str
