from tkinter import Toplevel, Frame, Button, Label, messagebox
from tkinter import TOP, X, LEFT, RIGHT
from components.named_entry import NamedEntry
import os.path

class DeveloperInfoPanel(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.company = NamedEntry(master=self, name="Company name", value=master.context["developer"]["company"])
        self.company.pack(side=TOP)
        self.organize = NamedEntry(master=self, name="Organization", value=master.context["developer"]["organize"])
        self.organize.pack(side=TOP)
        self.organize_unit = NamedEntry(master=self, name="Organizational unit", value=master.context["developer"]["organizeUnit"])
        self.organize_unit.pack(side=TOP)
        self.location = NamedEntry(master=self, name="Location", value=master.context["developer"]["location"])
        self.location.pack(side=TOP)
        self.state = NamedEntry(master=self, name="State", value=master.context["developer"]["state"])
        self.state.pack(side=TOP)
        self.country_code = NamedEntry(master=self, name="Country code", value=master.context["developer"]["countryCode"])
        self.country_code.pack(side=TOP)


class ProjectPanel(Frame):
    def __init__(self, master, parent_directory):
        super().__init__(master)
        self.parent_directory = parent_directory
        self.project_name = NamedEntry(master=self, name="Project name", value="", handle_value_change=self._handle_project_name_change)
        self.project_name.pack()
        self.workspace = NamedEntry(master=self, name="Workspace", value="")
        self.workspace.pack()
        self.resource_directory = NamedEntry(master=self, name="Resource directory", value="")
        self.resource_directory.pack()
        self.code_directory = NamedEntry(master=self, name="Code directory", value="")
        self.code_directory.pack()
        self.obj_directory = NamedEntry(master=self, name="Objective directory", value="")
        self.obj_directory.pack()
        self.bin_directory = NamedEntry(master=self, name="Bin directory", value="")
        self.bin_directory.pack()
        self.lib_directory = NamedEntry(master=self, name="Lib directory", value="")
        self.lib_directory.pack()
        self.docs_directory = NamedEntry(master=self, name="Docs directory", value="")
        self.docs_directory.pack()
        self.dex_file = NamedEntry(master=self, name="Dex file name", value="classes.dex")
        self.dex_file.pack()
        self.apk_file = NamedEntry(master=self, name="Apk file name", value="")
        self.apk_file.pack()

    def _handle_project_name_change(self, *args):
        project_name = self.project_name.value
        self.workspace.value = os.path.join(self.parent_directory, project_name)
        self.resource_directory.value = os.path.join(self.workspace.value, "res")
        self.code_directory.value = os.path.join(self.workspace.value, "src")
        self.obj_directory.value = os.path.join(self.workspace.value, "obj")
        self.bin_directory.value = os.path.join(self.workspace.value, "bin")
        self.lib_directory.value = os.path.join(self.workspace.value, "lib")
        self.docs_directory.value = os.path.join(self.workspace.value, "docs")
        self.apk_file.value = project_name + ".apk"


class ControlPanel(Frame):
    def __init__(self, master, ok_handler, cancel_handler):
        super().__init__(master)
        Label(self).pack(side=LEFT, fill=X)
        self.ok_button = Button(self, text="OK", bd=2, width=10, command=ok_handler)
        self.ok_button.pack(side=LEFT)
        Label(self).pack(side=RIGHT)
        self.cancel_button = Button(self, text="CANCEL", bd=2, width=10, command=cancel_handler)
        self.cancel_button.pack(side=RIGHT)
        Label(self).pack(side=RIGHT, fill=X)

class CreateProjectWindow(Toplevel):
    def __init__(self, master, context, project_parent_directory):
        super().__init__(master)
        self.master = master
        self.resizable(False, False)
        self.project_parent_directory = project_parent_directory
        self.context = context
        self.title("Creating android project")
        self._deploy_developer_info_panel()
        self._deploy_project_panel()
        self._deploy_control_panel()
        self.update()

    def _deploy_developer_info_panel(self):
        self.developer_panel = DeveloperInfoPanel(self)
        self.developer_panel.pack()

    def _deploy_project_panel(self):
        self.project_panel = ProjectPanel(self, self.project_parent_directory)
        self.project_panel.pack()

    def _deploy_control_panel(self):
        self.control_panel = ControlPanel(self, self._handle_ok, self._handle_cancel)
        self.control_panel.pack()

    def _handle_ok(self):
        self.context["developer"]["company"] = self.developer_panel.company.value
        self.context["developer"]["organize"] = self.developer_panel.organize.value
        self.context["developer"]["organizeUnit"] = self.developer_panel.organize_unit.value
        self.context["developer"]["location"] = self.developer_panel.location.value
        self.context["developer"]["state"] = self.developer_panel.state.value
        self.context["developer"]["countryCode"] = self.developer_panel.country_code.value
        self.context["project"]["project name"] = self.project_panel.project_name.value
        self.context["project"]["project directory"] = self.project_panel.workspace.value
        self.context["project"]["res directory"] = self.project_panel.resource_directory.value
        self.context["project"]["code directory"] = self.project_panel.code_directory.value
        self.context["project"]["obj directory"] = self.project_panel.obj_directory.value
        self.context["project"]["bin directory"] = self.project_panel.bin_directory.value
        self.context["project"]["docs directory"] = self.project_panel.docs_directory.value
        self.context["project"]["lib directory"] = self.project_panel.lib_directory.value
        self.context["project"]["dex file"] = self.project_panel.dex_file.value
        self.context["project"]["apk file"] = self.project_panel.apk_file.value
        self.destroy()

    def _handle_cancel(self):
        self.destroy()