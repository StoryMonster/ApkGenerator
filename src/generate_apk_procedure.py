import subprocess
from utils import get_all_java_files

class GenerateApkProcedure(object):
    def __init__(self, context, logger):
        self.context = context
        self.logger = logger
        self.company = self.context["position"]["company"]
        self.organize = self.context["position"]["organize"]
        self.organize_unit = self.context["position"]["organize unit"]
        self.location = self.context["position"]["location"]
        self.state = self.context["position"]["state"]
        self.country_code = self.context["position"]["country code"]
        self.project_name = self.context["project"]["project name"]
        self.res_dir = self.context["project"]["res directory"]
        self.code_dir = self.context["project"]["code directory"]
        self.obj_dir = self.context["project"]["obj directory"]
        self.bin_dir = self.context["project"]["bin directory"]
        self.lib_dir = self.context["project"]["lib directory"]
        self.docs_dir = self.context["project"]["docs directory"]
        self.dex_file = self.context["project"]["dex file"]
        self.apk_file = self.context["project"]["apk file"]
        self.workspace = self.context["project"]["project directory"]
        self.keytool = self.context["tools"]["keytool"]
        self.javac = self.context["tools"]["javac"]
        self.javadoc = self.context["tools"]["javadoc"]
        self.jarsigner = self.context["tools"]["jarsigner"]
        self.adb = self.context["tools"]["adb"]
        self.aapt = self.context["tools"]["aapt"]
        self.dx = self.context["tools"]["dx"]
        self.zipalign = self.context["tools"]["zipalign"]
        self.android_jar = self.context["tools"]["android.jar"]

    def run(self):
        self._create_key_store()
        self._create_R_file()
        self._compile_code()
        self._create_dex_file()
        self._create_unsigned_apk_file()
        self._sign_apk_file()
        self._zipalign_apk_file()

    def _execute_command(self, command):
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()[0], proc.communicate()[1]
        self.logger.write_line(out.decode("gbk"))
        self.logger.write_line(err.decode("gbk"))

    def _create_key_store(self):
        self.logger.write_line("Generating keystore file")
        command1 = [self.keytool,
                    "-genkeypair",
                    "-validity", "10000",
                    '-dname', f"CN={self.company}, OU={self.organize_unit}, O={self.organize}, L={self.location}, S={self.state}, C={self.country_code}",
                    "-keystore", f'{self.workspace}/{self.project_name}.keystore',
                    "-storepass", "password",
                    "-keypass", "password",
                    "-alias", f"{self.project_name}Key",
                    "-keyalg", "RSA", "-v",]
        command2 = [self.keytool,
                    "-importkeystore",
                    "-srckeystore", f'{self.workspace}/{self.project_name}.keystore',
                    "-destkeystore", f'{self.workspace}/{self.project_name}.keystore',
                    "-deststoretype", "pkcs12"]
        self._execute_command(command1)
        #subprocess.run(command2, capture_output=True))

    def _create_R_file(self):
        self.logger.write_line("Generate R.java")
        command = [self.aapt, "package",
                   "-v", "-f", "-m",
                   "-S", self.res_dir,
                   "-J", self.code_dir,
                   "-M", f'{self.workspace}/AndroidManifest.xml',
                   "-I", self.workspace]
        self._execute_command(command)

    def _compile_code(self):
        self.logger.write_line("Compile java files")
        java_files = get_all_java_files(self.code_dir)
        command = [self.javac, "-verbose",
                   "-d", self.obj_dir,
                   "-classpath", f'{self.android_jar};{self.obj_dir}',
                   "-sourcepath", self.code_dir]
        command.extend(java_files)
        self._execute_command(command)

    def _create_dex_file(self):
        self.logger.write_line("Generate dex file")
        command = [self.dx,
                   "--dex", "--verbose",
                   f'--output={self.bin_dir}/{self.dex_file}',
                   self.obj_dir, self.lib_dir]
        self._execute_command(command)

    def _create_unsigned_apk_file(self):
        self.logger.write_line("Generate unsigned apk file")
        command = [self.aapt, "package",
                   "-v", "-f",
                   "-M", f'{self.workspace}/AndroidManifest.xml',
                   "-S", self.res_dir,
                   "-I", self.android_jar,
                   "-F", f"{self.bin_dir}/unsigned.{self.apk_file}",
                   self.bin_dir]
        self._execute_command(command)
        
    def _sign_apk_file(self):
        self.logger.write_line("sign apk file")
        command = [self.jarsigner, "-verbose",
                   "-keystore", f"{self.workspace}/{self.project_name}.keystore",
                   "-storepass", "password",
                   "-keypass", "password",
                   "-signedjar", f"{self.bin_dir}/signed.{self.apk_file}",
                   f"{self.bin_dir}/unsigned.{self.apk_file}",
                   f"{self.project_name}Key"]
        self._execute_command(command)

    def _zipalign_apk_file(self):
        self.logger.write_line("zipalign apk file")
        command = [self.zipalign,
                   "-v", "-f", "4",
                   f"{self.bin_dir}/signed.{self.apk_file}",
                   f"{self.bin_dir}/{self.apk_file}"]
        self._execute_command(command)