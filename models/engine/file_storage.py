#!/usr/bin/python3
"""Contains definition of FileStorage class.
"""


import json
import os


class FileStorage:
    """Serialize instances to JSON file and deserializes JSON file to instances

    Attributes:
            __file_path (str): string - path to the JSON file.
            __objects (dict): dictionary - empty but will store all objects
                              by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as my_f:
            c = 0
            for key, value in self.__class__.__objects.items():
                if c > 0:
                    my_f.write("\n")
                obj_dict = {}
                obj_dict = {key: value.to_dict()}
                json.dump(obj_dict, my_f)
                c += 1

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists"""
        if os.path.exists(self.__class__.__file_path):
            stored_dicts = []
            with open(self.__class__.__file_path, encoding="utf-8") as my_file:
                for line in my_file:
                    try:
                        stored_dicts.append(json.loads(line))
                    except json.JSONDecodeError as e:
                        print(f"Error while parsing JSON: {e}")
            for stored_dict in stored_dicts:
                for key, value in stored_dict.items():
                    if "BaseModel" in key:
                        import models.base_model as base_model
                        self.__class__.__objects[key] = \
                            base_model.BaseModel(**value)
                    elif "User" in key:
                        import models.user as user
                        FileStorage.__objects[key] = user.User()
