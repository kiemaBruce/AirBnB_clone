#!/usr/bin/python3
"""Contains definition of Review class"""


class Review(BaseModel):
    """Attributes and methods of Review class

    Attributes:
            place_id (str): it is the Place.id
            user_id (str): it is the User.id
            text (str): review text.
    """

    place_id = ""
    user_id = ""
    text = ""
