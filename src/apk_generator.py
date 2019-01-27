from windows.main_window import MainWindow
from procedures.generate_apk_procedure import GenerateApkProcedure
from procedures.install_apk_procedure import InstallProcedure


class ApkGenerator(object):
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.main_window = MainWindow(self.context, handle_generate_apk=self.handle_generate_apk,
                                                    handle_install_apk=self.handle_install_apk)

    def handle_generate_apk(self, logger):
        proc = GenerateApkProcedure(self.context, logger)
        proc.start()

    def handle_install_apk(self, target, logger):
        proc = InstallProcedure(self.context, target, logger)
        proc.start()