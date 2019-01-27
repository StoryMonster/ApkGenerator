from tkinter import Toplevel, Frame, Button, Label, messagebox
from tkinter import TOP, X, LEFT, RIGHT
from components.named_entry import NamedEntry
import os.path

def _read_project_name(project_directory):
    items = project_directory.split("\\")
    for i in range(len(items)-1, -1, -1):
        if len(items[i]) > 0:
            return items[i]

class OrganizationPanel(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.company = NamedEntry(master=self, name="Company name", value="")
        self.company.pack(side=TOP)
        self.organize_unit = NamedEntry(master=self, name="Organizational unit", value="")
        self.organize_unit.pack(side=TOP)
        self.organize = NamedEntry(master=self, name="Organization", value="")
        self.organize.pack(side=TOP)
        self.location = NamedEntry(master=self, name="Location", value="")
        self.location.pack(side=TOP)
        self.state = NamedEntry(master=self, name="State", value="")
        self.state.pack(side=TOP)
        self.country_code = NamedEntry(master=self, name="Country code", value="")
        self.country_code.pack(side=TOP)

class ProjectPanel(Frame):
    def __init__(self, master, project_workspace):
        super().__init__(master)
        self.workspace = project_workspace
        self.default_project_name = _read_project_name(project_workspace)
        self.project_name = NamedEntry(master=self, name="Project name", value=self.default_project_name)
        self.project_name.pack()
        self.resource_directory = NamedEntry(master=self, name="Resource directory", value=os.path.join(self.workspace, "res"))
        self.resource_directory.pack()
        self.code_directory = NamedEntry(master=self, name="Code directory", value=os.path.join(self.workspace, "src"))
        self.code_directory.pack()
        self.obj_directory = NamedEntry(master=self, name="Objective directory", value=os.path.join(self.workspace, "obj"))
        self.obj_directory.pack()
        self.bin_directory = NamedEntry(master=self, name="Bin directory", value=os.path.join(self.workspace, "bin"))
        self.bin_directory.pack()
        self.lib_directory = NamedEntry(master=self, name="Lib directory", value=os.path.join(self.workspace, "lib"))
        self.lib_directory.pack()
        self.docs_directory = NamedEntry(master=self, name="Docs directory", value=os.path.join(self.workspace, "docs"))
        self.docs_directory.pack()
        self.dex_file = NamedEntry(master=self, name="Dex file name", value="classes.dex")
        self.dex_file.pack()
        self.apk_file = NamedEntry(master=self, name="Apk file name", value=self.default_project_name + ".apk")
        self.apk_file.pack()

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
    def __init__(self, context, project_directory):
        super().__init__()
        self.resizable(False, False)
        self.project_directory = project_directory
        self.context = context
        self.title("Project setting")
        self._deploy_orgnization_panel()
        self._deploy_project_panel()
        self._deploy_control_panel()
        self.update()

    def _deploy_orgnization_panel(self):
        self.organization_panel = OrganizationPanel(self)
        self.organization_panel.pack()

    def _deploy_project_panel(self):
        self.project_panel = ProjectPanel(self, self.project_directory)
        self.project_panel.pack()

    def _deploy_control_panel(self):
        self.control_panel = ControlPanel(self, self._handle_ok, self._handle_cancel)
        self.control_panel.pack()

    def _handle_ok(self):
        self.context["position"] = {}
        self.context["position"]["company"] = self.organization_panel.company.value
        self.context["position"]["organize"] = self.organization_panel.organize.value
        self.context["position"]["organize unit"] = self.organization_panel.organize_unit.value
        self.context["position"]["location"] = self.organization_panel.location.value
        self.context["position"]["state"] = self.organization_panel.state.value
        self.context["position"]["country code"] = self.organization_panel.country_code.value
        self.context["project"]["project name"] = self.project_panel.project_name.value
        self.context["project"]["project directory"] = self.project_directory
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