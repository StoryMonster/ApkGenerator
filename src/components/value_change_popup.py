from tkinter import Toplevel, Entry, Button, StringVar
from tkinter import LEFT
from copy import deepcopy


class ValueChangePopup(Toplevel):
    def __init__(self, master, env_item):
        super().__init__(master=master)
        self.resizable(False, False)
        self.master = master
        self.env_item = deepcopy(env_item)
        self.title(env_item.name)
        self.value = StringVar(self, env_item.value)
        entry = Entry(self, textvariable=self.value, width=30, bd=2)
        entry.pack(side=LEFT)
        ok = Button(self, text="OK", command=self._handle_ok, width=6, bd=2)
        ok.pack(side=LEFT)
        cancel = Button(self, text="CANCEL", command=self._handle_cancel, width=6, bd=2)
        cancel.pack(side=LEFT)
        self.update()
        self._is_value_changed = False

    def is_value_changed(self):
        return self._is_value_changed

    def get_changed_value(self):
        return self.env_item.value

    def _handle_cancel(self):
        self.destroy()

    def _handle_ok(self):
        if self.value.get() != self.env_item.value:
            self.env_item.change_value(self.value.get())
            self.is_value_changed = True
        self.destroy()
