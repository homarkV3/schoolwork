from database import Database

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class AddCommand(Command):
    def __init__(self, database, key, value):
        self.database = database
        self.key = key
        self.value = value
        self.executed = False

    def execute(self):
        success, msg = self.database.add(self.key, self.value)
        self.executed = success

    def undo(self):
        print(f"Undid AddCommand")
        if self.executed:
            self.database.remove(self.key)
            self.database.display()

class UpdateCommand(Command):
    def __init__(self, database, key, value):
        self.database = database
        self.key = key
        self.value = value
        self.original_value = None
        self.executed = False

    def execute(self):
        if self.key in self.database.data:
            self.original_value = self.database.data[self.key]
            success, _ = self.database.update(self.key, self.value)
            self.executed = success

    def undo(self):
        print(f"Undid UpdateCommand")
        if self.executed:
            self.database.update(self.key, self.original_value)
            self.database.display()

class RemoveCommand(Command):
    def __init__(self, database, key):
        self.database = database
        self.key = key
        self.removed_value = None
        self.executed = False

    def execute(self):
        if self.key in self.database.data:
            self.removed_value = self.database.data[self.key]
            success, _ = self.database.remove(self.key)
            self.executed = success

    def undo(self):
        print(f"Undid RemoveCommand")
        if self.executed:
            self.database.add(self.key, self.removed_value)
            self.database.display()

class MacroCommand(Command):
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute(self):
        print("Beginning a Macro")  # Print message at the start of macro execution
        for command in self.commands:
            command.execute()
        print("Ending a Macro\n")  # Print message at the end of macro execution

    def undo(self):
        print("Begin Undoing Macro\n") 
        for command in reversed(self.commands):
            command.undo()  
        print("End Undoing Macro\n")