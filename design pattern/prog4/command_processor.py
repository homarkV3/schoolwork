from database import Database
from commands import AddCommand, RemoveCommand, UpdateCommand, MacroCommand

class CommandProcessor:
    def __init__(self, command_file):
        self.command_file = command_file
        self.databases = {}
        self.command_stack = []

    def get_database(self, db_id):
        if db_id not in self.databases:
            self.databases[db_id] = Database(db_id)
        return self.databases[db_id]

    def create_command(self, cmd, db_id, *args):
        database = self.get_database(db_id)
        if cmd == "A":
            return AddCommand(database, *args)
        elif cmd == "U":
            return UpdateCommand(database, *args)
        elif cmd == "R":
            return RemoveCommand(database, args[0])
        
    def display_database(self, header="Contents of Databases:"):
        print(header)
        for db in self.databases.values():
            print(f"Database {db.id}:")
            db.display()

    def process_commands(self):
        macro_stack = []
        with open(self.command_file) as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                cmd = parts[0]

                if cmd == "B":
                    macro_command = MacroCommand()
                    if macro_stack:
                        macro_stack[-1].add_command(macro_command)
                    macro_stack.append(macro_command)
                    continue

                if cmd == "E" and macro_stack:
                    completed_macro = macro_stack.pop()
                    if not macro_stack:  # No enclosing macro, add to main stack
                        self.command_stack.append(completed_macro)
                    continue

                if cmd in ['A', 'U', 'R']:
                    command = self.create_command(cmd, parts[1], parts[2], " ".join(parts[3:]))
                    if macro_stack:
                        macro_stack[-1].add_command(command)
                    else:
                        self.command_stack.append(command)

        for command in self.command_stack:
            command.execute()
        self.display_database()

        for command in reversed(self.command_stack):
            command.undo()
        self.display_database()
