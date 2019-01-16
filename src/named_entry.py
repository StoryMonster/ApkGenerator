from tkinter import Frame, Label, Entry, StringVar
from tkinter import LEFT, RIGHT, X

class NamedEntry(Frame):
    def __init__(self, master, name, value):
        super().__init__(master)
        self.master = master
        self._name = name
        self._value = StringVar(self, value)
        self.label = Label(self, text=self._name, bd=2, width=20)
        self.label.pack(side=LEFT, fill=X)
        self.entry = Entry(self, textvariable=self._value, bd=2, width=60)
        self.entry.pack(side=RIGHT, fill=X)

    @property
    def value(self):
        return self._value.get()

    @value.setter
    def value(self, value):
        self._value.set(value)

    @property
    def name(self):
        return self._name
