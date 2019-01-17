from tkinter import Frame, Button, Label
from tkinter import X, LEFT, RIGHT


class OkCancelPanel(Frame):
    def __init__(self, master, handle_ok, handle_cancel):
        super().__init__(master)
        Label(self).pack(side=LEFT, fill=X)
        self.ok_button = Button(self, text="  OK  ", bd=2, command=handle_ok)
        self.ok_button.pack(side=LEFT)
        Label(self).pack(side=RIGHT)
        self.cancel_button = Button(self, text="CANCEL", bd=2, command=handle_cancel)
        self.cancel_button.pack(side=RIGHT)
        Label(self).pack(side=RIGHT, fill=X)
