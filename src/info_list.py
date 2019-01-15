from tkinter import Listbox, Scrollbar, messagebox
from tkinter import VERTICAL, RIGHT, Y, W, X, SINGLE, TOP, BOTH, DISABLED, NORMAL
from env_item import EnvItem
from info_list_popup_dialog import InfoListPopupDialog

class InfoList(Listbox):
    def __init__(self, master=None, **cwt):
        y_scrollar_bar = Scrollbar(master, orient=VERTICAL)
        y_scrollar_bar.pack(side=RIGHT, fill=Y)
        super().__init__(master=master, yscrollcommand=y_scrollar_bar.set, bd=5, selectmode=SINGLE, exportselection=False, **cwt)
        y_scrollar_bar.config(command=self.yview)
        self.bind("<Double-Button-1>", lambda event: self._handle_double_click())
        self.environs = {}
        self.append_env_item(EnvItem(name="project directory"))
        self.append_env_item(EnvItem(name="javac"))
        self.append_env_item(EnvItem(name="javadoc"))
        self.append_env_item(EnvItem(name="jarsigner"))
        self.append_env_item(EnvItem(name="adb"))
        self.append_env_item(EnvItem(name="aapt"))
        self.append_env_item(EnvItem(name="dx"))
        self.append_env_item(EnvItem(name="zipalign"))
        self.append_env_item(EnvItem(name="keytool"))
        self.append_env_item(EnvItem(name="android.jar"))
        self.popup_dialog = None

    def _get_env_item_by_index(self, index):
        elem = self.get(index, index)
        name = elem[0].split(":")[0].strip()
        return self.get_env_item(name)

    def _handle_double_click(self):
        if self.popup_dialog is not None: return
        index = self.curselection()[0]
        env_item = self._get_env_item_by_index(index)
        self.popup_dialog = InfoListPopupDialog(self, env_item)
        self.master.wait_window(self.popup_dialog)
        self.popup_dialog = None

    def append_env_item(self, item):
        self.environs[item.name] = item
        self.insert("end", item)

    def change_env_item_value(self, name, value):
        index = 0
        for item in self.get(0, self.size()-1):
            if item == str(self.environs[name]):
                break
            index += 1
        self.environs[name].value = value
        self.delete(index)
        self.insert(index, self.environs[name])

    def get_env_item(self, name):
        if name in self.environs:
            return self.environs[name]
        return None
