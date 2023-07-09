#!/usr/bin/python3
"""Command interpreter entry point module."""

import cmd


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

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def postloop(self):
        """Print a message after exiting the program."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
