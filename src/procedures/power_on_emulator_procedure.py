import subprocess

class PowerOnEmulatorProcedure(object):
    def __init__(self, avd, adb, logger):
        self.avd = avd
        self.logger = logger
        self.adb = adb

    def run(self):
        self._power_on_emulator()

    def _power_on_emulator(self):
        self.logger.write_line(f"Power on the avd {self.avd}")
        command = [self.adb, "-wipe-data", "-avd", self.avd]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = proc.communicate()
        self.logger.write_line(result[0].decode("gbk"))
        self.logger.write_line(result[1].decode("gbk"))
