import pygraphviz as pgv

def create_uml_diagram():
    G = pgv.AGraph(strict=True, directed=True)

    # Adding classes as nodes
    classes = [
        "CommandProcessor", "Database", "Command", "AddCommand", 
        "RemoveCommand", "UpdateCommand", "MacroCommand", "main"
    ]
    for cls in classes:
        G.add_node(cls, shape='box', color='lightblue', style='filled')

    # Adding relationships
    G.add_edge("main", "CommandProcessor", label="creates and uses")
    G.add_edge("CommandProcessor", "Database", label="manages")
    G.add_edge("CommandProcessor", "Command", label="uses")
    G.add_edge("Command", "AddCommand", label="parent of")
    G.add_edge("Command", "RemoveCommand", label="parent of")
    G.add_edge("Command", "UpdateCommand", label="parent of")
    G.add_edge("Command", "MacroCommand", label="parent of")
    G.add_edge("MacroCommand", "Command", label="aggregates", dir="back")

    # Special relationships for command classes to Database
    G.add_edge("AddCommand", "Database", label="uses")
    G.add_edge("RemoveCommand", "Database", label="uses")
    G.add_edge("UpdateCommand", "Database", label="uses")

    # Render the graph to a file (output as PNG)
    output_path = "/mnt/data/full_codebase_uml.png"
    G.draw(output_path, prog='dot')

    output_path
if __name__ == "__main__":
    create_uml_diagram()
