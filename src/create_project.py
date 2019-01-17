from tkinter import Toplevel, Frame
from components.named_entry import NamedEntry
from components.ok_cancel_panel import OkCancelPanel


class ProjectInfoPanel(Frame):
    def __init__(self, master, context):
        super().__init__(master)
        self.master = master
        self.context = context

class CreateProjectWindow(Toplevel):
    def __init__(self, master, context):
        super().__init__(master)
        self.master = master
        self.context = context



