from tkinter import Tk, messagebox, Menu, Frame, Scrollbar, Listbox, Button, Text
from tkinter import LEFT, RIGHT, TOP, BOTTOM, BOTH, VERTICAL, Y, W, X, SINGLE, HORIZONTAL
from tkinter.filedialog import askdirectory
from tkinter.font import Font
from windows.create_project_window import CreateProjectWindow
from generate_apk_procedure import GenerateApkProcedure
from install_apk_procedure import InstallProcedure
from common.utils import put_widget_at_center_of_screen
from common.env_item import EnvItem
from components.info_list import InfoList
import os


class LogPanel(Frame):
    def __init__(self):
        super().__init__()
        log_x_scrollar_bar = Scrollbar(self, orient=HORIZONTAL)
        log_x_scrollar_bar.pack(side=BOTTOM, fill=X)
        log_y_scrollar_bar = Scrollbar(self, orient=VERTICAL)
        log_y_scrollar_bar.pack(side=RIGHT, fill=Y)
        self.log_area = Text(self, bd=5, wrap="none",
                             font=Font(family="Times New Roman", size=12, weight="normal"),
                             xscrollcommand=log_x_scrollar_bar.set, yscrollcommand=log_y_scrollar_bar.set)
        self.log_area.pack(anchor="center", fill=BOTH, expand=1)
        log_x_scrollar_bar.config(command=self.log_area.xview)
        log_y_scrollar_bar.config(command=self.log_area.yview)

    def _see_at_end(self):
        self.log_area.see("end")

    def set_text(self, text):
        self.log_area.delete("1.0", "end")
        self.log_area.insert("1.0", text)
        self._see_at_end()

    def clear(self):
        self.log_area.delete("1.0", "end")
        self._see_at_end()

    def write_line(self, line):
        self.log_area.insert("end", line + "\n")
        self._see_at_end()

    def write(self, text):
        self.log_area.insert("end", text)
        self._see_at_end()


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


class InfoPanel(Frame):
    def __init__(self):
        super().__init__()
        self.info_list = InfoList(self)
        self.info_list.pack(side=TOP, fill=BOTH, expand=1)

    def get_env_item(self, name):
        return self.info_list.get_env_item(name)


class MainWindow(Tk):
    def __init__(self, context, handle_generate_apk=None, handle_install_apk=None):
        super().__init__()
        self.context = context
        self.handle_generate_apk = handle_generate_apk
        self.handle_install_apk = handle_install_apk
        self.title("ApkGenerator")
        self.resizable(False, False)
        self.project_setting_window = None
        self._add_menu_bar()
        self.info_panel = InfoPanel()
        self.info_panel.pack(side=LEFT, fill=BOTH, expand=1)
        self.control_panel = ControlPanel()
        self.control_panel.pack(side=LEFT, fill=BOTH, expand=1)
        self.control_panel.generate_button.bind("<Button-1>", lambda event : self._handle_generate_apk_file())
        self.control_panel.install_on_device_button.bind("<Button-1>", lambda event : self._handle_install_on_device())
        self.control_panel.install_on_emulator_button.bind("<Button-1>", lambda event : self._handle_install_on_emulator())
        self.control_panel.uninstall_button.bind("<Button-1>", lambda event : self._handle_uninstall_app())
        self.log_panel = LogPanel()
        self.log_panel.pack(side=RIGHT, fill=BOTH)
        self._apply_context()
        self.geometry("900x600+100+100")
        self.update()
        put_widget_at_center_of_screen(self)

    def _add_menu_bar(self):
        menubar = Menu(self)
        menubar.add_command(label="Open project", command=self._handle_create_project)
        menubar.add_command(label="Edit environment", command=None)
        self.config(menu=menubar)

    def _handle_create_project(self):
        if self.project_setting_window is not None: return
        self.project_setting_window = CreateProjectWindow(self.context, os.path.abspath(askdirectory()))
        put_widget_at_center_of_screen(self.project_setting_window)
        self.wait_window(self.project_setting_window)
        self.project_setting_window = None
        for key in self.context["project"]:
            self.info_panel.info_list.append_item(key, self.context["project"][key])
        for key in self.context["position"]:
            self.info_panel.info_list.append_item(key, self.context["position"][key])

    def _apply_context(self):
        for tool_name in self.context["tools"]:
            if os.path.isfile(str(self.context["tools"][tool_name])):
                env_item = self.info_panel.get_env_item(tool_name)
                if env_item is not None:
                    self.info_panel.info_list.change_env_item_value(tool_name, self.context["tools"][tool_name])

    def _handle_generate_apk_file(self):
        if self.handle_generate_apk is not None:
            self.handle_generate_apk(logger=self.log_panel)

    def _handle_install_on_device(self):
        if self.handle_install_apk is not None:
            self.handle_install_apk(target="device", logger=self.log_panel)

    def _handle_install_on_emulator(self):
        if self.handle_install_apk is not None:
            self.handle_install_apk(target="emulator", logger=self.log_panel)

    def _handle_uninstall_app(self):
        pass
