#!/usr/bin/env python3
import cmd
import models
import json
import datetime


class HBNBCommand(cmd.Cmd):
    """The console class where everything comes together"""
    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    classList = ["BaseModel", "User"]
    attributes = ["created_at", "updated_at", "id"]
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def EOF(self, arg):
        """Quits the program"""
        return True

    def emptyline(self):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        pass

    def help_quit(self):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        print("Quit command to exist the program")

    def help_EOF(self):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        print("Quits the program with sending EOF message")

    def do_help(self, arg):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        print("Documented commands (type help <topic>):\n\
                ========================================\n\
                EOF help quit")

    def do_create(self, arg):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        classname = arg.strip()
        if not arg:
            print("** class name missing **")
            return
        if arg not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        argument = argprocess(arg)
        details = {class_name: argument[0], class_id: argument[1]}
        if len(details) == 0:
            print("** class name missing **")
            return
        if not details.class_id:
            print("** instance id missing")
            return
        if details.class_name is not in classList:
            print("** class doesn't exist **")
            return
        instance = search_instance_by_id(details.class_id)
        if instance not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[instance])

    def do_destroy(self, arg):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        argument = argprocess(arg)
        details = {class_name: argument[0], class_id: argument[1]}
        if len(details) == 0:
            print("** class name missing **")
            return
        if not details.class_id:
            print("** instance id missing")
            return
        if details.class_name is not in classList:
            print("** class doesn't exist **")
            return
        instance = search_instance_by_id(details.class_id)
        if instance is None:
            print("** no instance found **")
        else:
            del storage.all()[instance]
            storage.save()

    def do_all(self, arg):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        argument = argprocess(arg)
        if argument is not in classList:
            print("** class doesn't exist **")
            return
        data = models.storage.all()
        filtered_instances = []
        for key, instances in data.items():
            if not class_name or instance.__class__.__name__ == argument:
                filtered_instances.append(instance)
        print([str(instance) for instance in filtered_instances])

    def do_update(self, arg):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        argument = argprocess(arg)
        if len(argument) == 0:
            print("** class name missing **")
            return
        if len(argument) < 2:
            print("** instance id missing **")
            return
        if len(argument) < 3:
            print("** attribute name missing **")
            return
        if len(argument) < 4:
            print("** value missing **")
            return
        # If everything is here:
        details = {class_name: argument[0], class_id: argument[1],
                   attribute: argument[2], attribute_val: argument[3]}
        if details.class_name not in classList:
            print("** class doesn't exist **")
            return
        if details.id not in storage.all():
            print("** no instance found **")
            return
        if attribute_value.isdigit():
            attribute_value = int(attribute_value)
        else:
            try:
                attribute_value = float(attribute_value)
            except ValueError:
                pass
        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def argprocess(sentence):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        words = sentence.split()
        stripped_words = [word.strip() for word in words]
        return stripped_words

    def is_valid_uuid(id_string):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        try:
            uuid.UUID(id_string)
            return True
        except ValueError:
            return False

    def search_instance_by_id(instance_id):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        # Open the JSON file for reading
        with open('file.json', 'r') as file:
            # Load the JSON data
            data = json.load(file)

            # Check if the instance ID exists in the JSON data
            if instance_id in data:
                # Retrieve the details of the instance based on its ID
                instance_details = data[instance_id]
                return instance_details
            else:
                # Return None if the instance ID is not found
                return None


if __name__ == "__main__":
    HBNBCommand.cmdloop()
