from tkinter import Frame, Scrollbar, Text
from tkinter import HORIZONTAL, VERTICAL, BOTTOM, RIGHT, BOTH, X, Y


class LogPanel(Frame):
    def __init__(self):
        super().__init__()
        log_x_scrollar_bar = Scrollbar(self, orient=HORIZONTAL)
        log_x_scrollar_bar.pack(side=BOTTOM, fill=X)
        log_y_scrollar_bar = Scrollbar(self, orient=VERTICAL)
        log_y_scrollar_bar.pack(side=RIGHT, fill=Y)
        self.log_area = Text(self, bd=5, wrap="none", xscrollcommand=log_x_scrollar_bar.set, yscrollcommand=log_y_scrollar_bar.set)
        self.log_area.pack(anchor="center", fill=BOTH, expand=1)
        log_x_scrollar_bar.config(command=self.log_area.xview)
        log_y_scrollar_bar.config(command=self.log_area.yview)

    def _see_at_end(self):
        pass

    def set_text(self, text):
        self.log_area.delete("1.0", "end")
        self.log_area.insert("1.0", text)
        self._see_at_end()

    def append_text(self, text):
        self.log_area.insert("end", text)
        self._see_at_end()

    def clear(self):
        self.log_area.delete("1.0", "end")
        self._see_at_end()

    def write_line(self, line):
        self.log_area.insert("end", "\n")
        self.log_area.insert("end", line)
        self._see_at_end()

    def write(self, text):
        self.log_area.insert("end", text)
        self._see_at_end()

