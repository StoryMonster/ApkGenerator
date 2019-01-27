from tkinter import Tk, messagebox, Menu, Frame, Scrollbar, Listbox, Button, Text
from tkinter import LEFT, RIGHT, TOP, BOTTOM, BOTH, VERTICAL, Y, W, X, SINGLE, HORIZONTAL
from tkinter.font import Font
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


class InfoPanel(Frame):
    def __init__(self):
        super().__init__()
        self.info_list = InfoList(self)
        self.info_list.pack(side=TOP, fill=BOTH, expand=1)

    def get_env_item(self, name):
        return self.info_list.get_env_item(name)


class MainWindow(Tk):
    def __init__(self, context, handle_generate_apk=None,
                                handle_install_apk=None,
                                handle_create_project=None,
                                handle_clean_project=None):
        super().__init__()
        self.context = context
        self.handle_generate_apk = handle_generate_apk
        self.handle_install_apk = handle_install_apk
        self.handle_create_project = handle_create_project
        self.handle_clean_project = handle_clean_project
        self.title("ApkGenerator")
        self.resizable(False, False)
        self.project_setting_window = None
        self._add_menu_bar()
        self.info_panel = InfoPanel()
        self.info_panel.pack(side=LEFT, fill=BOTH, expand=1)
        self.log_panel = LogPanel()
        self.log_panel.pack(side=RIGHT, fill=BOTH)
        self.update_info_list()
        self.geometry("900x600+100+100")
        self.update()
        put_widget_at_center_of_screen(self)

    def _add_menu_bar(self):
        menubar = Menu(self)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Create project", command=self.handle_create_project)
        file_menu.add_command(label="Open project", command=None)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=None)
        file_menu.add_command(label="Exit", command=None)

        project_menu = Menu(menubar, tearoff=0)
        project_menu.add_command(label="Build", command=self._handle_generate_apk_file)
        project_menu.add_command(label="Clear", command=self._handle_clean_project)
        project_menu.add_command(label="Install on device", command=self._handle_install_on_device)
        project_menu.add_command(label="Uninstall", command=self._handle_uninstall_app)

        emulator_menu = Menu(menubar, tearoff=0)
        emulator_menu.add_command(label="Power on/off emulator", command=None)
        emulator_menu.add_command(label="Install on emulator", command=None)
        emulator_menu.add_command(label="Uninstall from emulator", command=None)
        emulator_menu.add_command(label="list avalible emulators", command=None)

        setting_menu = Menu(menubar, tearoff=0)
        setting_menu.add_command(label="setting1", command=None)
        setting_menu.add_command(label="setting2", command=None)
        setting_menu.add_command(label="setting3", command=None)
        setting_menu.add_command(label="setting4", command=None)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Project", menu=project_menu)
        menubar.add_cascade(label="Emulator", menu=emulator_menu)
        menubar.add_cascade(label="Setting", menu=setting_menu)
        self.config(menu=menubar)

    def update_info_list(self):
        if "project" in self.context:
            for key in self.context["project"]:
                self.info_panel.info_list.append_item(key, self.context["project"][key])
        if "position" in self.context:
            for key in self.context["position"]:
                self.info_panel.info_list.append_item(key, self.context["position"][key])
        if "tools" in self.context:
            for key in self.context["tools"]:
                self.info_panel.info_list.append_item(key, self.context["tools"][key])

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
        self.log_panel.write_line("Handle uninstall app")

    def _handle_clean_project(self):
        self.handle_clean_project(logger=self.log_panel)