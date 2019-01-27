import subprocess
import os.path
from threading import Thread


class InstallProcedure(Thread):
    def __init__(self, context, target, logger):
        super().__init__()
        '''
        target can be: emulator or device
        '''
        self.target = target
        self.context = context
        self.logger = logger
        self.adb = self.context["tools"]["adb"]
        self.apk_file = self.context["project"]["apk file"]
        self.bin_dir = self.context["project"]["bin directory"]

    def run(self):
        if self.target == "emulator":
           self._install_on_emulator()
           return
        self._install_on_device()

    def _execute_command(self, command):
        self.logger.write_line(" ".join(command))
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = proc.communicate()
        self.logger.write_line(result[0].decode("gbk"))
        self.logger.write_line(result[1].decode("gbk"))

    def _install_on_emulator(self):
        # check emulator status
        command = [self.adb, "-e", "install", os.path.join(self.bin_dir, self.apk_file)]
        self.logger.write_line(f"Install {self.apk_file} to emulator: ")
        self._execute_command(command)

    def _install_on_device(self):
        # check device status
        command = [self.adb, "-d", "install", os.path.join(self.bin_dir, self.apk_file)]
        self.logger.write_line(f"Install {self.apk_file} to device")
        self._execute_command(command)
