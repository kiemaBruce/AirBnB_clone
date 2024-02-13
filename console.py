#!/usr/bin/python3
"""Contains entry point of command interpreter.
"""


import cmd


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

    def emptyline(self):
        """Does nothing for empty line + enter"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
