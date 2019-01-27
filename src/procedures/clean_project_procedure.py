import os
import subprocess
from common.utils import get_R_java_file, remove_all_under_folder


class CleanProjectProcedure(object):
    def __init__(self, context, logger):
        self.context = context
        self.logger = logger

    def run(self):
        self._remove_keystore_files()
        self._remove_R_file()
        self._remove_obj_files()
        self._remove_bin_files()

    def _execute_command(self, command):
        self.logger.write_line(" ".join(command))
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = proc.communicate()
        self.logger.write_line(result[0].decode("gbk"))
        self.logger.write_line(result[1].decode("gbk"))

    def _remove_keystore_files(self):
        keystore_file = os.path.join(self.context["project"]["project directory"], self.context["project"]["project name"] + ".keystore")
        keystore_file_old = os.path.join(self.context["project"]["project directory"], self.context["project"]["project name"] + ".keystore.old")
        if os.path.exists(keystore_file):
            self.logger.write_line(f"remove {keystore_file}")
            os.remove(keystore_file)
        if os.path.exists(keystore_file_old):
            self.logger.write_line(f"remove {keystore_file_old}")
            os.remove(keystore_file_old)
    
    def _remove_R_file(self):
        R_jave = get_R_java_file(self.context["project"]["code directory"])
        if R_jave is not None:
            self.logger.write_line("remove R.java")
            os.remove(R_jave)

    def _remove_obj_files(self):
        obj_directory = self.context["project"]["obj directory"]
        self.logger.write_line(f"remove files under {obj_directory}")
        remove_all_under_folder(obj_directory)

    def _remove_bin_files(self):
        bin_directory = self.context["project"]["bin directory"]
        self.logger.write_line(f"remove files under {bin_directory}")
        remove_all_under_folder(bin_directory)
