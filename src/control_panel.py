from tkinter import Frame, TOP, BOTTOM, BOTH, X
from tkinter import Button


class ControlPanel(Frame):
    def __init__(self):
        super().__init__(bd=3)
        self.uninstall_button = Button(master=self, text="Uninstall", bd=5)
        self.uninstall_button.pack(side=BOTTOM, fill=X)
        self.install_on_emulator_button = Button(master=self, text="Install On Emulator", bd=5)
        self.install_on_emulator_button.pack(side=BOTTOM, fill=X)
        self.install_on_device_button = Button(master=self, text="Install On Device", bd=5)
        self.install_on_device_button.pack(side=BOTTOM, fill=X)
        self.generate_button = Button(master=self, text="GENERATE", bd=5)
        self.generate_button.pack(side=BOTTOM, fill=X)

