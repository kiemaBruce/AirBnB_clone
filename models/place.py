#!/usr/bin/python3
"""Contains definition of Place class"""


class Place(BaseModel):
    """Attributes and methods of Place class

    Attributes:
            city_id (str): it is the City.id
            user_id (str): it is the User.id
            name (str): name of the place
            description (str): description of the place.
            number_rooms (int): number of rooms.
            number_bathrooms (int): number of bathrooms.
            max_guest (int): the maximum number of guests.
            price_by_night (int): price by night.
            latitude (float): latitude of the place.
            longitude (float): longitude of the place.
            amenity_ids (list): it is the list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
