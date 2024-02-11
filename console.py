#!/usr/bin/python3
"""Console"""
import cmd

from models import storage, base_model, user


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

        if args[0] not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return

        instance = self.models[args[0]]()
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

        if args[0] not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return

        if len(args) == 1:
            print(INSTANCE_ID_MISSING_MESSAGE)
            return

        instances = storage.all()
        try:
            result = instances[args[1]]
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

        if args[0] not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return

        elif len(args) == 1:
            print(INSTANCE_ID_MISSING_MESSAGE)
            return

        instances = storage.all()
        if args[1] in instances:
            del instances[args[1]]
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
            if len(args) == 0 or args[0] == obj["__class__"]:
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

        class_name = args[0]
        if class_name not in self.models.keys():
            print(CLASS_NOT_EXIST_MESSAGE)
            return

        if len(args) == 1:
            print(INSTANCE_ID_MISSING_MESSAGE)
            return

        instance_id = args[1]
        if instance_id not in storage.all():
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
        instance = instances[instance_id]
        instance[attribute_name] = attribute_value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
