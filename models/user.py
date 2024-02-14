#!/usr/bin/python3
"""Contains definition of User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """Contains attributes and methods for a user.

    Attributes:
            email (str): user's email address.
            password (str): user's password.
            first_name (str): user's first name.
            last_name (str): user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes object"""
        super().__init__(*args, **kwargs)
