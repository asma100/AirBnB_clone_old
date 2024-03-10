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

    def default(self, line):
        """Default behavior of the console."""
        try:
            args = line.split('.')
            cls_name = args[0]
            command = args[1].split('(')
            method = command[0]

            methods = {
                'all': self.do_all,
                'show': self.do_show,
                'count': self.do_count,
                'update': self.do_update,
                'destroy': self.do_destroy
            }

            if method in methods.keys():
                return methods[method]("{} {}".format(cls_name, ''))
        except IndexError:
            print("*** Unkown syntax: {}".format(line))

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
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
        """Updates the values to keys of the class."""
        args = arg.split()
        objdict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for key, v in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str,
                                                              int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(v)
                else:
                    obj.__dict__[key] = v
        storage.save()

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

    def do_count(self, arg):
        """Prints the number of instances of a class"""
        count = 0
        args = arg.split()
        if args:
            classname = args[0]
            if classname not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            if classname in HBNBCommand.classes:
                for i in storage.all().values():
                    if i.__class__.__name__ == classname:
                        count += 1
                print(count)
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
