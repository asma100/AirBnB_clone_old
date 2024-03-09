from models.base_model import BaseModel
"""Amenity  Model """
class Amenity(BaseModel):
    """Represnts the Amenity model"""
    name = " "
  def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        if len(args) == 1:
            print("** instance id is missing **")
        if len(arg) == 2:
            print("** attribute name missing **")
        if len(arg) == 3:
            print("** value missing **")

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