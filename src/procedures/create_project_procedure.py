from windows.create_project_window import CreateProjectWindow
from tkinter.filedialog import askdirectory
from common.utils import put_widget_at_center_of_screen
import os

class CreateProjectProcedure(object):
    def __init__(self, context, parent_window):
        self.window = None
        self.context = context
        self.parent_window = parent_window

    def run(self):
        self._show_window()
        self._add_basic_files_or_folders()
        self._create_project_file()

    def _show_window(self):
        '''
        '''
        if self.window is not None: return
        self.window = CreateProjectWindow(self.parent_window, self.context, os.path.abspath(askdirectory()))
        put_widget_at_center_of_screen(self.window)
        self.parent_window.wait_window(self.window)
        self.window = None

    def _add_basic_files_or_folders(self):
        '''
        '''
        pass

    def _create_project_file(self):
        '''
        '''
        pass
