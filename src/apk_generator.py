from tkinter import Tk, messagebox, Menu
from tkinter import LEFT, RIGHT, TOP, BOTTOM, BOTH
from tkinter.filedialog import askdirectory
from log_panel import LogPanel
from control_panel import ControlPanel
from info_panel import InfoPanel
from generate_apk_procedure import GenerateApkProcedure
from install_apk_procedure import InstallProcedure
from project_setting import ProjectSettingWindow
from utils import put_widget_at_center_of_screen
import os


class ApkGenerator(Tk):
    def __init__(self, context):
        super().__init__()
        self.context = context
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
        menubar.add_command(label="Open project", command=self._handle_open_project)
        menubar.add_command(label="Edit environment", command=None)
        self.config(menu=menubar)

    def _handle_open_project(self):
        if self.project_setting_window is not None: return
        self.project_setting_window = ProjectSettingWindow(self.context, os.path.abspath(askdirectory()))
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
        proc = GenerateApkProcedure(self.context, self.log_panel)
        proc.run()

    def _handle_install_on_device(self):
        proc = InstallProcedure(self.context, "device", self.log_panel)
        proc.run()

    def _handle_install_on_emulator(self):
        proc = InstallProcedure(self.context, "emulator", self.log_panel)
        proc.run()

    def _handle_uninstall_app(self):
        pass
