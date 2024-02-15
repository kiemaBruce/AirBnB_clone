#!/usr/bin/python3
"""Contains definition of City class"""


from models.base_model import BaseModel


class City(BaseModel):
    """Attributes and methods of City class

    Attributes:
            state_id (str): the state id. It is State.id
            name (str): the name of the city.

    """

    state_id = ""
    name = ""
