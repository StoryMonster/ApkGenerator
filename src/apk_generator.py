from windows.main_window import MainWindow
from procedures.generate_apk_procedure import GenerateApkProcedure
from procedures.install_apk_procedure import InstallProcedure
from procedures.create_project_procedure import CreateProjectProcedure
from procedures.clean_project_procedure import CleanProjectProcedure
from procedures.power_on_emulator_procedure import PowerOnEmulatorProcedure
#from procedures.open_project_procedure import OpenProjectProcedure


class ApkGenerator(object):
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.main_window = MainWindow(self.context, handle_generate_apk=self.handle_generate_apk,
                                                    handle_install_apk=self.handle_install_apk,
                                                    handle_create_project=self.handle_create_project,
                                                    handle_clean_project=self.handle_clean_project,
                                                    handle_power_on_emulator=self.handle_power_on_emulator,
                                                    handle_open_project = self.handle_open_project)
        self.main_window.show_configuration()

    def run(self):
        self.main_window.mainloop()

    def handle_generate_apk(self, logger):
        proc = GenerateApkProcedure(self.context, logger)
        proc.start()

    def handle_install_apk(self, target, logger):
        proc = InstallProcedure(self.context, target, logger)
        proc.start()

    def handle_create_project(self):
        proc = CreateProjectProcedure(context=self.context, parent_window=self.main_window)
        proc.run()
        #self.main_window.update_info_list()

    def handle_clean_project(self, logger):
        proc = CleanProjectProcedure(self.context, logger)
        proc.run()

    def handle_power_on_emulator(self, logger):
        self.context["tools"]["emulator"] = "C:/Program Files/AndroidSDK/tools/emulator.exe"
        proc = PowerOnEmulatorProcedure(avd="MyPhone", adb=self.context["tools"]["emulator"], logger=logger)
        proc.run()

    def handle_open_project(self):
        OpenProjectProcedure(context=self.context).run()
        self.main_window.update_info_list()
