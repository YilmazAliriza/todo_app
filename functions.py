FILEPATH = "toDos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(todos, filepath=FILEPATH):
    """ Write the to-do item's list in the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos)


if __name__ == "__main__":
    print("Hello")
