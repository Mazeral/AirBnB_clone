#!/usr/bin/env python3
import cmd
import models
import json


class HBNBCommand(cmd.Cmd):
    classList = ["BaseModel"]
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quits the program"""
        return True
    
    def EOF(self, arg):
        """Quits the program"""
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        print("Quit command to exist the program")

    def help_EOF(self):
        print("Quits the program with sending EOF message")

    def do_help(self, arg):
        print("Documented commands (type help <topic>):\n\
                ========================================\n\
                EOF help quit")

    def do_create(self, arg):
        classname = arg.strip()
        if not classname:
            print("** class name missing **")
            return
        if hasattr(models, arg):
            cls = getattr(models, classname)
            if isinstance(cls, type):
                new_instance = cls()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
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
            return str(instance)

    def do_destroy(self):
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
            with open("models/engine/file.json", 'r') as f:
                data = load.json(f)
                if data[details.class_id]:
                    del data[details.class_id]
                else:
                    print("** no instance found **")
                    return

    def do_all(self):
        pass

    def argprocess(sentence):
        words = sentence.split()
        stripped_words = [word.strip() for word in words]
        return stripped_words
    
def is_valid_uuid(id_string):
    try:
        uuid.UUID(id_string)
        return True
    except ValueError:
        return False

def search_instance_by_id(instance_id):
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
