from tkinter import Tk, messagebox, Menu, Frame, Scrollbar, Listbox, Button, Text
from tkinter import LEFT, RIGHT, TOP, BOTTOM, BOTH, VERTICAL, Y, W, X, SINGLE, HORIZONTAL
from tkinter.font import Font
from common.utils import put_widget_at_center_of_screen


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


class MainWindow(Tk):
    def __init__(self, context, handle_generate_apk=None,
                                handle_install_apk=None,
                                handle_create_project=None,
                                handle_clean_project=None,
                                handle_power_on_emulator=None,
                                handle_open_project=None):
        super().__init__()
        self.context = context
        self.handle_generate_apk = handle_generate_apk
        self.handle_install_apk = handle_install_apk
        self.handle_create_project = handle_create_project
        self.handle_clean_project = handle_clean_project
        self.handle_power_on_emulator = handle_power_on_emulator
        self.handle_open_project = handle_open_project
        self.title("ApkGenerator")
        self.project_setting_window = None
        self._add_menu_bar()
        self.log_panel = LogPanel()
        self.log_panel.pack(side=LEFT, fill=BOTH, expand=1)
        self.geometry("900x600+100+100")
        self.update()
        put_widget_at_center_of_screen(self)

    def show_configuration(self):
        for key in self.context["tools"]:
            self.log_panel.write_line(f"{key}:{self.context['tools'][key]}")

    def _add_menu_bar(self):
        menubar = Menu(self)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="create project", command=self.handle_create_project)
        file_menu.add_command(label="open project", command=self.handle_open_project)
        file_menu.add_separator()
        file_menu.add_command(label="save", command=None)
        file_menu.add_command(label="exit", command=None)

        project_menu = Menu(menubar, tearoff=0)
        project_menu.add_command(label="build", command=self._handle_generate_apk_file)
        project_menu.add_command(label="clear", command=self._handle_clean_project)
        project_menu.add_command(label="install on device", command=self._handle_install_on_device)
        project_menu.add_command(label="uninstall", command=self._handle_uninstall_app)

        emulator_menu = Menu(menubar, tearoff=0)
        emulator_menu.add_command(label="power on/off emulator", command=self._handle_power_on_emulator)
        emulator_menu.add_command(label="install on emulator", command=None)
        emulator_menu.add_command(label="uninstall from emulator", command=None)
        emulator_menu.add_command(label="list avalible emulators", command=None)

        setting_menu = Menu(menubar, tearoff=0)
        setting_menu.add_command(label="font", command=None)
        setting_menu.add_command(label="setting2", command=None)
        setting_menu.add_command(label="setting3", command=None)
        setting_menu.add_command(label="setting4", command=None)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Project", menu=project_menu)
        menubar.add_cascade(label="Emulator", menu=emulator_menu)
        menubar.add_cascade(label="Setting", menu=setting_menu)
        self.config(menu=menubar)

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

    def _handle_power_on_emulator(self):
        self.handle_power_on_emulator(logger=self.log_panel)
