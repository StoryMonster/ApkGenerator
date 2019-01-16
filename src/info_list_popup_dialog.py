from tkinter import Toplevel, Entry, Button, StringVar
from tkinter import LEFT, RIGHT

class InfoListPopupDialog(Toplevel):
    def __init__(self, master, env_item):
        super().__init__(master=master)
        self.resizable(False, False)
        self.master = master
        self.env_item = env_item
        self.title(env_item.name)
        self._text = StringVar(self, env_item.value)
        entry = Entry(self, textvariable=self._text, width=30, bd=2)
        entry.pack(side=LEFT)
        ok = Button(self, text="OK", command=self._handle_ok, width=6, bd=2)
        ok.pack(side=LEFT)
        cancel = Button(self, text="CANCEL", command=self._handle_cancel, width=6, bd=2)
        cancel.pack(side=LEFT)
        self.update()

    def _handle_cancel(self):
        self.destroy()

    def _handle_ok(self):
        self.master.change_env_item_value(self.env_item.name, self._text.get())
        self.destroy()
