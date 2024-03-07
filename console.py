#!/usr/bin/python3
"""Defines the Console class"""

import cmd
import models

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command Interperter
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amentity", "Place", "Review"]
    def do_quit(self,arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def handle_empty_lines(self, arg):
        """passes empty lines"""
        return False

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if arg == "":
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            print(new_instance.id)
            new_instance.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        if len(args) < 2:
            print("** instance id is missing **")
        if args[0] in HBNBCommand.classes:
            dictionary = storage.all()
            if len(args) >= 2:
                key = args[0] + '.' + args[1]
                if key in dictionary:
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
