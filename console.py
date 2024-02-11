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
UNKOWN_COMMAND_MESSAGE = "*** Unknown syntax:"


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

    def default(self, line):
        """Default"""
        pattern = line.split('.')
        if len(pattern) == 2:
            class_name, command_with_args = pattern
            if command_with_args.startswith("all()"):
                self.do_all(class_name)
            elif command_with_args.startswith("count()"):
                self.do_count(class_name)
            elif (
                command_with_args.startswith("show(")
                and
                command_with_args.endswith(")")
            ):
                instance_id = command_with_args[5:-1].strip('"\'')
                self.do_show(f"{class_name} {instance_id}")
            elif (
                command_with_args.startswith("destroy(")
                and
                command_with_args.endswith(")")
            ):
                instance_id = command_with_args[8:-1].strip('"\'')
                self.do_destroy(f"{class_name} {instance_id}")
            elif (
                "update(" in command_with_args
                and
                command_with_args.endswith(")")
            ):
                args_str = command_with_args[7:-1]
                self.do_update_by_command(class_name, args_str)
            else:
                print("*** Unknown syntax:", line)
        else:
            print("*** Unknown syntax:", line)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_count(self, class_name):
        """Counts the number of instances of a class."""
        count = 0
        instances = storage.all()
        for instance in instances.values():
            if instance.__class__.__name__ == class_name:
                count += 1
        print(count)

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
        instance_full_id = f"{model_name}.{instance_id}"
        if instance_full_id in instances:
            del instances[instance_full_id]
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
        setattr(instance, attribute_name, attribute_value)
        storage.save()

    def do_update_by_command(self, class_name, args_str):
        """Parses the update command from the default method and calls do_update."""
        args = args_str.split(', ')
        if len(args) < 3:
            print("** Invalid arguments **")
            return

        instance_id = args[0].strip('"\'')
        attribute_name = args[1].strip('"\'')
        attribute_value = args[2].strip('"\'')
        self.do_update(f"{class_name} {instance_id} {attribute_name} {attribute_value}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
