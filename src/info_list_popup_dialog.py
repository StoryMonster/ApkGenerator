from tkinter import Toplevel, Entry, Button, StringVar
from tkinter import LEFT, RIGHT

class InfoListPopupDialog(Toplevel):
    def __init__(self, master, env_item):
        super().__init__(master=master)
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
        self._central_self()

    def _handle_cancel(self):
        self.destroy()

    def _handle_ok(self):
        self.master.change_env_item_value(self.env_item.name, self._text.get())
        self.destroy()

    def _central_self(self):
        px = self.master.winfo_rootx()
        py = self.master.winfo_rooty()
        pw = self.master.winfo_width()
        ph = self.master.winfo_height()
        w = self.winfo_width()
        h = self.winfo_height()
        x = int(px + (pw-w)/2)
        y = int(py + (ph-h)/2)
        self.geometry(f"+{x}+{y}")
