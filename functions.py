FILEPATH = 'todos.txt'


def get_todos(filepath_in=FILEPATH):
    """
    reads the contents of 'todos.txt',
    and returns those contents to a list variable
    """
    with open(filepath_in, "r") as file_local:
        todos_out = file_local.readlines()
    return todos_out


def write_todos(todos_in, filepath_in=FILEPATH):
    """
    writes the items in f_todos to file 'todos.txt'
    no return value
    """
    with open(filepath_in, "w") as todos_file:
        todos_file.writelines(todos_in)
    return


