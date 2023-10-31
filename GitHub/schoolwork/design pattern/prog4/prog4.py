import sys

# Database Class
class Database:
    def __init__(self, id):
        self.id = id
        self.data = {}

    def getID(self):
        return self.id

    def add(self, key, value):
        if key in self.data:
            print(f"Error: Key '{key}' already exists.")
            return False
        else:
            self.data[key] = value
            return True

    def get(self, key):
        return self.data.get(key, None)

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
            return True
        else:
            print(f"Error: Key '{key}' does not exist.")
            return False

    def remove(self, key):
        if key in self.data:
            del self.data[key]
            return True
        else:
            print(f"Error: Key '{key}' does not exist.")
            return False

    def display(self):
        print(f"Database {self.id}:")
        for key, value in self.data.items():
            print(f"{key}| {value}")

# Command Classes
class Command:
    def __init__(self):
        self.successful = False

    def execute(self):
        pass

    def undo(self):
        pass

    def __str__(self):
        return "Command"

class AddCommand(Command):
    def __init__(self, db, key, value):
        super().__init__()
        self.db = db
        self.key = key
        self.value = value

    def execute(self):
        self.successful = self.db.add(self.key, self.value)

    def undo(self):
        if self.successful:
            self.db.remove(self.key)

    def __str__(self):
        return "AddCommand"

class MacroCommand(Command):
    def __init__(self):
        super().__init__()
        self.commands = []

    def add_command(self, cmd):
        self.commands.append(cmd)

    def execute(self):
        print("Beginning a Macro")
        for cmd in self.commands:
            cmd.execute()
        print("Ending a Macro")
        self.successful = all(cmd.successful for cmd in self.commands)

    def undo(self):
        print("Begin Undoing Macro")
        for cmd in reversed(self.commands):
            cmd.undo()
        print("End Undoing Macro")

    def __str__(self):
        return "MacroCommand"

class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, cmd):
        cmd.execute()
        if cmd.successful: 
            self.history.append(cmd)
        else:
            print(f"Command {cmd} was not successful and will not be added to the history.")

    def undo_last(self):
        if self.history:
            cmd = self.history.pop()
            print(f"Undid {cmd}")
            cmd.undo()
        else:
            print("No commands to undo.")

def main(file_path):
    invoker = Invoker()
    databases = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            command_type, db_id, key, *value = parts
            value = ' '.join(value)  

            if db_id not in databases:
                databases[db_id] = Database(db_id)

            db = databases[db_id]

            if command_type == 'A':
                cmd = AddCommand(db, key, value)
                invoker.execute_command(cmd)

    for db in databases.values():
        db.display()

    while invoker.history:
        invoker.undo_last()
        for db in databases.values():
            db.display()

    for db in databases.values():
        db.display()

if __name__ == "__main__":
    main(sys.argv[1])  # Pass the file name through command-line arguments
