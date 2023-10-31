import pygraphviz as pgv

def create_uml_diagram():
    # Create a new graph
    graph = pgv.AGraph(strict=False, directed=True)

    # Define the appearance of the graph
    graph.node_attr['shape'] = 'record'
    graph.node_attr['style'] = 'filled'
    graph.node_attr['fillcolor'] = '#F5F5F5'

    # Adding classes with their attributes and methods
    graph.add_node('Database', label='{{Database|- id : String\n- data : Dictionary|+ __init__(id: String)\n+ getID(): String\n+ add(key: String, value: String): Boolean\n+ get(key: String): String\n+ update(key: String, value: String): Boolean\n+ remove(key: String): Boolean\n+ display(): void}}')

    graph.add_node('Command', label='{{Command|- successful : Boolean|+ execute(): void\n+ undo(): void}}')

    graph.add_node('AddCommand', label='{{AddCommand|- db : Database\n- key : String\n- value : String|+ __init__(db: Database, key: String, value: String)\n+ execute(): void\n+ undo(): void}}')

    graph.add_node('Invoker', label='{{Invoker|- history : List|+ __init__()\n+ execute_command(cmd: Command)\n+ undo_last()}}')

    # Defining relationships (Generalization and Association)
    graph.add_edge('AddCommand', 'Command')  # Generalization (Inheritance)
    graph.add_edge('AddCommand', 'Database', dir='back')  # Association

    # The rest of the classes like RemoveCommand, UpdateCommand, etc., will follow a similar pattern

    # Save the graph to a file
    graph.draw('uml_diagram.png', prog='dot')  # This creates a PNG file in the current directory

if __name__ == "__main__":
    create_uml_diagram()



+----------------------------------+
|             Database             |
+----------------------------------+
| - id: String                     |
| - data: Dictionary               |
+----------------------------------+
| + __init__(id: String)           |
| + getID(): String                |
| + add(key: String, value: String): Boolean |
| + get(key: String): String       |
| + update(key: String, value: String): Boolean |
| + remove(key: String): Boolean   |
| + display(): void                |
+----------------------------------+

+----------------------------------+
|             Command              |
+----------------------------------+
| - successful: Boolean            |
+----------------------------------+
| + __init__()                     |
| + execute(): void                |
| + undo(): void                   |
| + __str__(): String              |
+----------------------------------+
           Λ
           |
    +------+-----------------+
    |                        |
+---|------>  AddCommand      +--------------------------+
|   +-----------------------+                            |
|   | - db: Database        |                            |
|   | - key: String         |                            |
|   | - value: String       |                            |
|   +-----------------------+                            |
|   | + __init__(db: Database, key: String, value: String) |  +---------+
|   | + execute(): void     |                            |  |         |
|   | + undo(): void        |                            +--+ Invoker |
|   | + __str__(): String   |                               |         |
|   +-----------------------+                               +---------+
|                                                              |
+--|-------------------+  MacroCommand  <----------------------+
   +----------------------------------+
   | - commands: List[Command]        |
   +----------------------------------+
   | + __init__()                     |
   | + add_command(cmd: Command)      |
   | + execute(): void                |
   | + undo(): void                   |
   | + __str__(): String              |
   +----------------------------------+
