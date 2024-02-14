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

    @staticmethod
    def check_duplicates(check_key):
        """Checks if a BaseModel object in __objects is already in json file.

        Args:
            check_key (str): the key in __objects of the object to be checked.

        Return:
            bool: True if the key is already in the file and False if it isn't.
        """
        stored_dicts = []
        with open(FileStorage.__file_path, encoding="utf-8") as my_file:
            for line in my_file:
                try:
                    stored_dicts.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Error while parsing JSON: {e}")
        for stored_dict in stored_dicts:
            if check_key in stored_dict:
                return True
        return False

    def all(self):
        """Returns the dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj
        # print("New object")

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as my_f:
            for key, value in self.__class__.__objects.items():
                # if not FileStorage.check_duplicates(key):
                if len(self.__class__.__objects) > 1:
                    my_f.write("\n")
                obj_dict = {}
                obj_dict = {key: value.to_dict()}
                json.dump(obj_dict, my_f)

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
                    import models.base_model as base_model
                    self.__class__.__objects[key] = \
                        base_model.BaseModel(**value)
