from menu import Menu
from notebook import Note, Notebook


if __name__ == "__main__":
    notebook = Notebook()

    print(dir(Note))
    print(dir(Menu))
    print(dir(Notebook))

    print(isinstance(notebook, object))
    print(isinstance(notebook.notes, object))

