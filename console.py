#!/usr/bin/python3
"""Defines the Console class"""

import cmd
#import models
import sys

#from models.base_model import BaseModel
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
#from models.user import User


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
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
        # Check for class existence (optional)
        if class_name not in ["User", "Amenity","BaseModel","State","City","Place","Review"]:
                print("** class doesn't exist **")
                return
        
        dictionary = storage.all()
        if len(args) >= 2:
                key = class_name + '.' + instance_id
                if key in dictionary:
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]

            # Check for class existence (optional)
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            # Construct key and delete object
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
            
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        if len(args) < 2:
            print("** instance id is missing **")
        if len(args) == 4:
            class_name, instance_id, attr_name, attr_value = args[:4]
            if class_name in HBNBCommand.classes:
                dictionary = storage.all()
                if len(args) >= 2:
                    key = class_name + '.' + instance_id
                    if key in dictionary:
                        dictionary[key].__dict__[attr_name] = attr_value
                        dictionary[key].save()
                    else:
                        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
