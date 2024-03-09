#!/usr/bin/python3
"""Defines the Console class"""

import cmd
import sys

from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command Interperter.
    """
    prompt = "(hbnb) "
    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Amentity",
               "Place",
               "Review"]

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def emptyarg(self):
        """passes empty args"""
        return

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
            return

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict[key])


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            key = f"{class_name}.{instance_id}"
            obj_dict = storage.all()
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        try:
            if not arg:
                raise SyntaxError()
            my_list = split(arg, " ")
            if my_list[0] not in HBNBCommand.classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        instances = storage.all()

        if len(args) == 0:
            print([str(instance) for instance in instances.values()])
        elif args:
            if args[0] in HBNBCommand.classes:
                object_list = [str(instance) for instance in instances.values()
                               if instance.__class__.__name__ == args[0]]
                if object_list:
                    print(object_list)
                else:
                    print("[]")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
