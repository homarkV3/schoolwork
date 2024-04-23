class FileSystemNode:
    def __init__(self, name):
        self.name = name

    def list(self):
        pass

    def listall(self):
        pass

    def count(self):
        pass

    def countall(self):
        pass

class File(FileSystemNode):
    def list(self, prefix=""):
        print(prefix + self.name)

    def listall(self, prefix=""):
        self.list(prefix)

    def count(self):
        return 1

    def countall(self):
        return self.count()

class Directory(FileSystemNode):
    def __init__(self, name, parent=None):
        super().__init__(name)
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def list(self, prefix=""):
        print(" ".join(child.name for child in self.children))

    def listall(self, prefix=""):
        print(prefix + self.name + ":")
        for child in self.children:
            child.listall(prefix + "   ")

    def count(self):
        return sum(child.count() for child in self.children if isinstance(child, File))

    def countall(self):
        return sum(child.countall() for child in self.children)

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

def parse_directory_structure(lines, parent=None, level=1):
    children = []
    while lines:
        line = lines[0]
        indent_level = line.count("   ")
        if indent_level < level:
            break
        line = line.strip()
        if line.endswith(":"):
            dir_name = line[:-1]
            directory = Directory(dir_name, parent)
            children.append(directory)
            lines.pop(0)  
            directory.children = parse_directory_structure(lines, directory, level + 1)
        else:
            children.append(File(line))
            lines.pop(0)  
    return children

def load_file_structure(filename):
    with open(filename, "r") as f:
        lines = [line.rstrip() for line in f if line.strip()]  
    top_dir_name = lines.pop(0)[:-1]  
    top_dir = Directory(top_dir_name)
    top_dir.children = parse_directory_structure(lines, top_dir)
    return top_dir

class FileSystemExplorer:
    def __init__(self, root):
        self.current_dir = root
        self.path_stack = []

    def process_command(self, command):
        cmd_parts = command.split()
        if cmd_parts[0] == "list":
            self.current_dir.list()
        elif cmd_parts[0] == "listall":
            self.current_dir.listall()
        elif cmd_parts[0] == "chdir":
            if len(cmd_parts) != 2:
                print("Invalid command. Usage: chdir <directory_name>")
                return True
            dir_name = cmd_parts[1]
            new_dir = self.current_dir.get_child(dir_name)
            if new_dir and isinstance(new_dir, Directory):
                self.path_stack.append(self.current_dir)
                self.current_dir = new_dir
            else:
                print("no such directory")
        elif cmd_parts[0] == "up":
            if self.path_stack:
                self.current_dir = self.path_stack.pop()
            else:
                print("Already at the root")
        elif cmd_parts[0] == "count":
            print(self.current_dir.count())
        elif cmd_parts[0] == "countall":
            print(self.current_dir.countall())
        elif cmd_parts[0] == "q":
            return False 
        else:
            print("Invalid command")
        return True

if __name__ == "__main__":
    root = load_file_structure("directory.dat")
    explorer = FileSystemExplorer(root)
    running = True
    while running:
        command = input(f"{explorer.current_dir.name}> ").strip()
        running = explorer.process_command(command)
