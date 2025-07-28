FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-dos."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the list of to-dos to a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

