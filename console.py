#!/usr/bin/python3
"""Contains entry point of command interpreter.
"""


import models.base_model as base_model
import cmd
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class

    Attributes:
            prompt (str): displayed before each command.
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def do_create(self, line):
        """Creates a new instance, saves it and prints the id"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            classes = ["BaseModel", "User"]
            if line not in classes:
                print("** class doesn't exist **")
            else:
                if line == "BaseModel":
                    bm1 = base_model.BaseModel()
                    bm1.save()
                    print(bm1.id)

    def do_show(self, line):
        """Prints string representation of instance.

        This string representation is based on the class name and instance id.

        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            split_str = line.split(sep=" ")
            if split_str[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(split_str) < 2:
                    print("** instance id missing **")
                else:
                    s_key = f"{split_str[0]}.{split_str[1]}"
                    if s_key not in storage.all():
                        print("** no instance found **")
                    else:
                        print(storage.all()[s_key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if len(line) == 0:
            print("** class name missing **")
        else:
            split_str = line.split(sep=" ")
            if split_str[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(split_str) < 2:
                    print("** instance id missing **")
                else:
                    s_key = f"{split_str[0]}.{split_str[1]}"
                    if s_key not in storage.all():
                        print("** no instance found **")
                    else:
                        with open("file.json", encoding='utf-8') as my_file:
                            parsed_list = []
                            for line in my_file:
                                try:
                                    parsed_list.append(json.loads(line))
                                except json.JSONDecodeError as e:
                                    print(f"Error while parsing JSON: {e}")
                        for index, item in enumerate(parsed_list):
                            for key in item:
                                if s_key == key:
                                    rm_index = index
                        parsed_list.pop(rm_index)
                        with open("file.json", mode="w",
                                  encoding='utf-8') as my_file:
                            for index, item in enumerate(parsed_list):
                                if index > 0:
                                    my_file.write("\n")
                                json.dump(item, my_file)
                        del storage.all()[s_key]

    def do_all(self, line):
        """Prints string representation of all instances.

        If no argument is given, it prints all instances of BaseModel class.

        """
        c = 0
        if line:
            if line == "BaseModel":
                all_list = []
                for key in storage.all():
                    all_list.append(f"{storage.all()[key]}")
                c = 1
            else:
                print("** class doesn't exist **")
        else:
            all_list = []
            for key in storage.all():
                all_list.append(str(storage.all()[key]))
            c = 1
        if c == 1:
            print(all_list)

    @staticmethod
    def strip_quotes(check_str):
        """Strips surrounding quotations from a string.

        Args:
            check_str (str): the string to be processed.

        Return:
            str: The string sans the enclosing quotations if it was surrounded
                 by double quotes. If the string had no enclosing quotation
                 marks then it is left untouched. If it had either opening or
                 closing quotation marks only then the string is left
                 untouched. Both single and double quotation marks are dealt
                 with.
        """
        if check_str[0] == '"':
            if check_str[-1] == '"':
                end_index = len(check_str) - 1
                return check_str[1: end_index]
        elif check_str[0] == "'":
            if check_str[-1] == "'":
                end_index = len(check_str) - 1
                return check_str[1: end_index]
        return check_str

    def do_update(self, line):
        """Updates an instance based on the class name and id.

        Attributes are added if new or updated if they already exist. The
        attributes: id, created_at, updated_at are never updated with this
        method.
        """
        if not line:
            print("** class name missing **")
        else:
            strs_list = line.split(" ")
            if strs_list[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(strs_list) == 1:
                    print("** instance id missing **")
                else:
                    s_key = f"{strs_list[0]}.{strs_list[1]}"
                    if s_key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(strs_list) == 2:
                            print("** attribute name missing **")
                        else:
                            if len(strs_list) == 3:
                                print("** value missing **")
                            else:
                                forbidden_attrs = [
                                                      "id",
                                                      "created_at",
                                                      "updated_at"
                                                  ]
                                current_obj = storage.all()[s_key]
                                rem_quotes = \
                                    HBNBCommand.strip_quotes(strs_list[3])
                                if strs_list[2] not in forbidden_attrs:
                                    setattr(
                                        current_obj,
                                        strs_list[2],
                                        rem_quotes
                                    )
                                    current_obj.save()

    def emptyline(self):
        """Does nothing for empty line + enter"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
