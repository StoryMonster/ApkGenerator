from tkinter import Frame, Scrollbar, Listbox
from tkinter import VERTICAL, RIGHT, Y, W, X, SINGLE, TOP, BOTH
from env_item import EnvItem
from info_list import InfoList


class InfoPanel(Frame):
    def __init__(self):
        super().__init__()
        self.info_list = InfoList(self)
        self.info_list.pack(side=TOP, fill=BOTH, expand=1)

    def get_env_item(self, name):
        return self.info_list.get_env_item(name)

