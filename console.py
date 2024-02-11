#!/usr/bin/python3
"""Console"""
import cmd

from models import amenity
from models import base_model
from models import city
from models import place
from models import storage
from models import review
from models import state
from models import user


CLASS_MISSING_MESSAGE = "** class name missing **"
CLASS_NOT_EXIST_MESSAGE = "** class doesn't exist **"
INSTANCE_ID_MISSING_MESSAGE = "** instance id missing **"
NO_INSTANCE_FOUND_MESSAGE = "** no instance found **"
ATTRIBUTE_NAME_MISSING_MESSAGE = "** attribute name missing **"
ATTRIBUTE_VALUE_MISSING_MESSAGE = "** value missing **"


class HBNBCommand(cmd.Cmd):
    """AirBnB Clone console"""
    prompt = '(hbnb) '
    models = {
        base_model.BaseModel.__name__: base_model.BaseModel,
        amenity.Amenity.__name__: amenity.Amenity,
        city.City.__name__: city.City,
        place.Place.__name__: place.Place,
        review.Review.__name__: review.Review,
        state.State.__name__: state.State,
        user.User.__name__: user.User,
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel
            saves it to the JSON file, and prints the id

        Usage:
            create <class name>
        """
        args = arg.split()
        if len(args) == 0:
            print(CLASS_MISSING_MESSAGE)
            return

        model_name = args[0]
        if model_name not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return

        instance = self.models[model_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """ Prints the string representation of
            an instance based on the class name and id.

        Usage:
            show <class name> <instance id>
        """
        args = arg.split()
        if len(args) == 0:
            print(CLASS_MISSING_MESSAGE)
            return

        model_name = args[0]
        if model_name not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return

        if len(args) == 1:
            print(INSTANCE_ID_MISSING_MESSAGE)
            return

        instances = storage.all()
        instance_id = args[1]
        try:
            result = instances[f"{model_name}.{instance_id}"]
        except KeyError:
            print(NO_INSTANCE_FOUND_MESSAGE)
        else:
            print(result)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            and saves the change into the JSON file.

        Usage:
            destroy <class name> <instance id>
        """
        args = arg.split()
        if len(args) == 0:
            print(CLASS_MISSING_MESSAGE)
            return

        model_name = args[0]
        if model_name not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return

        elif len(args) == 1:
            print(INSTANCE_ID_MISSING_MESSAGE)
            return

        instances = storage.all()
        instance_id = args[1]
        if instance_id in instances:
            del instances[f"{model_name}.{instance_id}"]
            storage.save()
        else:
            print(NO_INSTANCE_FOUND_MESSAGE)

    def do_all(self, arg):
        """ Prints all string representation of all instances
            based or not on the class name.

        Usage:
            all
            all <class name>
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return
        instances = []
        for obj in storage.all().values():
            if len(args) == 0 or args[0] == obj.__class__.__name__:
                instances.append(str(obj))
        print(instances)

    def do_update(self, arg):
        """ Updates an instance based on the class name
            and id by adding or updating attribute.

        Usage:
            update <class name> <instance id> <attr name> <attr value>
        """
        args = arg.split()
        if len(args) == 0:
            print(CLASS_MISSING_MESSAGE)
            return

        model_name = args[0]
        if model_name not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return

        if len(args) == 1:
            print(INSTANCE_ID_MISSING_MESSAGE)
            return

        instance_id = args[1]
        instance_full_id = f"{model_name}.{instance_id}"
        if instance_full_id not in storage.all():
            print(NO_INSTANCE_FOUND_MESSAGE)
            return

        if len(args) == 2:
            print(ATTRIBUTE_NAME_MISSING_MESSAGE)
            return

        if len(args) == 3:
            print(ATTRIBUTE_VALUE_MISSING_MESSAGE)
            return

        attribute_name = args[2]
        attribute_value = args[3]
        instances = storage.all()
        instance = instances[instance_full_id]
        instance[attribute_name] = attribute_value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
