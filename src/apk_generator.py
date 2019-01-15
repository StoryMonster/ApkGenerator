from tkinter import Tk, messagebox, Menu
from tkinter import LEFT, RIGHT, TOP, BOTTOM, BOTH
from tkinter.filedialog import askdirectory
from log_panel import LogPanel
from control_panel import ControlPanel
from info_panel import InfoPanel
import os


def is_android_project_valid(project_directory):
    return True

def is_java_home_valid(java_home_path):
    return java_home_path is not None and len(java_home_path) > 0

def is_android_home_valid(android_home_path):
    return android_home_path is not None and len(android_home_path) > 0


class ApkGenerator(Tk):
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.title("ApkGenerator")
        self._center_self()
        self._add_menu_bar()
        self.info_panel = InfoPanel()
        self.info_panel.pack(side=TOP, fill=BOTH, expand=1)
        self.control_panel = ControlPanel()
        self.control_panel.pack(side=TOP, fill=BOTH, expand=1)
        self.control_panel.generate_button.bind("<Button-1>", lambda event : self._handle_generate_apk_file())
        self.control_panel.install_on_device_button.bind("<Button-1>", lambda event : self._handle_install_on_device())
        self.control_panel.install_on_emulator_button.bind("<Button-1>", lambda event : self._handle_install_on_emulator())
        self.control_panel.uninstall_button.bind("<Button-1>", lambda event : self._handle_uninstall_app())
        self.log_panel = LogPanel()
        self.log_panel.pack(side=BOTTOM, fill=BOTH, expand=1)
        self._apply_context()

    def _center_self(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        client_width = int(screen_width * 0.5)
        client_heith = int(screen_height * 0.6)
        client_x_position = int((screen_width - client_width)/2)
        client_y_position = int((screen_height - client_heith)/2)
        self.geometry('{}x{}'.format(client_width, client_heith))
        self.geometry('+{}+{}'.format(client_x_position, client_y_position))

    def _add_menu_bar(self):
        menubar = Menu(self)
        menubar.add_command(label="Open project", command=self._handle_open_project)
        menubar.add_command(label="Edit environment", command=None)
        self.config(menu=menubar)

    def _handle_open_project(self):
        self.project_directory = askdirectory()
        self.info_panel.info_list.change_env_item_value("project directory", self.project_directory)
        if not is_android_project_valid(self.project_directory):
            messagebox.showerror(title="invalid project", message="Your android project cannot be compiled")
            return
        ## configure other attributes

    def _apply_context(self):
        for tool_name in self.context["tools"]:
            if os.path.isfile(str(self.context["tools"][tool_name])):
                env_item = self.info_panel.get_env_item(tool_name)
                if env_item is not None:
                    self.info_panel.info_list.change_env_item_value(tool_name, self.context["tools"][tool_name])

    def _configure_project_information(self):
        self.context["project"] = {}
        self.context["project"]["unsigned_apk_name"] = "output.unsigned.apk"
        self.context["project"]["signed_apk_name"] = "output.signed.apk"
        self.context["project"]["aigned_apk_name"] = "output.apk"
        self.context["project"]["dex_name"] = "output.dex"
        self.context["project"]["project_directory"] = self.project_directory

    def _handle_generate_apk_file(self):
        self.log_panel.append_line("clicked generate")

    def _handle_install_on_device(self):
        self.log_panel.append_line("clicked install on device")

    def _handle_install_on_emulator(self):
        self.log_panel.append_line("clicked install on emulator")

    def _handle_uninstall_app(self):
        self.log_panel.append_line("clicked uninstall app")
