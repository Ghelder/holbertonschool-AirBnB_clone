#!/usr/bin/python3
"""Command interpreter entry point module."""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class represents the command line
    interface for the HBNB program."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Print help message for the quit command."""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Handle EOF (End of File) input."""
        return True

    # def emptyline(self):
    #     """Do nothing when an empty line is entered."""
    #     pass

    def postloop(self):
        """Print a message after exiting the program."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                obj = eval(arg)()
                obj.save()
                print(obj.id)
            except NameError:
                print("** class doesn't exist **")

    classes = {"BaseModel": BaseModel}

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        # key = "{}.{}".format(class_name, instance_id)
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        # key = "{}.{}".format(class_name, instance_id)
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name."""
        if not arg:
            instances = storage.all().values()
        elif arg in self.classes:
            instances = [
                v for k, v in storage.all().items() if k.startswith(arg)
            ]
        else:
            print("** class doesn't exist **")
            return

        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(storage.all()[key], args[-2], args[-1].replace('"', ""))
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
