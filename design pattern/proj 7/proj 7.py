class Visitor:
    def visit_file(self, file):
        raise NotImplementedError

    def visit_directory(self, directory):
        raise NotImplementedError


class ListVisitor(Visitor):
    def visit_file(self, file):
        print(file.name)

    def visit_directory(self, directory):
        print(directory.name + ":")


class ListAllVisitor(Visitor):
    def __init__(self, prefix=""):
        self.prefix = prefix

    def visit_file(self, file):
        print(self.prefix + file.name)

    def visit_directory(self, directory):
        print(self.prefix + directory.name + ":")
        new_prefix = self.prefix + "   "
        for child in directory.children:
            child.accept(ListAllVisitor(new_prefix))


class CountVisitor(Visitor):
    def __init__(self):
        self.count = 0

    def visit_file(self, file):
        self.count += 1

    def visit_directory(self, directory):
        for child in directory.children:
            child.accept(self)

    def get_count(self):
        return self.count


class FileSystemNode:
    def accept(self, visitor):
        raise NotImplementedError


class File(FileSystemNode):
    def accept(self, visitor):
        visitor.visit_file(self)


class Directory(FileSystemNode):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def accept(self, visitor):
        visitor.visit_directory(self)

    def accept_children(self, visitor):
        for child in self.children:
            child.accept(visitor)


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

    def process_command(self, command):
        cmd_parts = command.split()
        if cmd_parts[0] == "list":
            self.current_dir.accept(ListVisitor())
        elif cmd_parts[0] == "listall":
            self.current_dir.accept(ListAllVisitor())
        elif cmd_parts[0] == "count":
            visitor = CountVisitor()
            self.current_dir.accept(visitor)
            print(visitor.get_count())
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
