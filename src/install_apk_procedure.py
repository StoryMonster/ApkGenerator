import subprocess
import os.path


class InstallProcedure(object):
    def __init__(self, context, target, logger):
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

    def _install_on_emulator(self):
        # check emulator status
        command = [self.adb, "-e", "install", os.path.join(self.bin_dir, self.apk_file)]
        self.logger.write_line(f"Install {self.apk_file} to emulator: ")
        self.logger.write_line(" ".join(command))
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()[0], proc.communicate()[1]
        self.logger.write_line(out.decode("gbk"))
        self.logger.write_line(err.decode("gbk"))

    def _install_on_device(self):
        # check device status
        command = [self.adb, "-d", "install", os.path.join(self.bin_dir, self.apk_file)]
        self.logger.write_line(f"Install {self.apk_file} to device")
        self.logger.write_line(" ".join(command))
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()[0], proc.communicate()[1]
        self.logger.write_line(out.decode("gbk"))
        self.logger.write_line(err.decode("gbk"))
