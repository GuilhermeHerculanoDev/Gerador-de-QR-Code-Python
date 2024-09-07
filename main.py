from customtkinter import *
from Controller.controller import Controller
from Model.model import Model
from View.view import View


def main():
    root = CTk()
    view = View(root)
    model = Model()
    controller = Controller(view, model)

    root.mainloop()


if __name__ == "__main__":
    main()