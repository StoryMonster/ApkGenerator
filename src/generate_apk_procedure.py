import subprocess
import os
import sys

class GenerateApkProcedure(object):
    def __init__(self, context, logger):
        self.context = context
        self.logger = logger
        self.workspace = context["project"]["project_directory"]

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
        command1 = [self.context["tools"]["keytool"],
                    "-genkeypair",
                    "-validity", "10000",
                    '-dname', "CN=dochen, OU=dochen, O=organisation, L=location, S=state, C=country code",
                    "-keystore", f'{self.workspace}/AndroidTest.keystore',
                    "-storepass", "password",
                    "-keypass", "password",
                    "-alias", "AndroidTestKey",
                    "-keyalg", "RSA", "-v",]
        command2 = [self.context["tools"]["keytool"],
                    "-importkeystore",
                    "-srckeystore", f'{self.workspace}/AndroidTest.keystore',
                    "-destkeystore", f'{self.workspace}/AndroidTest.keystore',
                    "-deststoretype", "pkcs12"]
        self._execute_command(command1)
        #subprocess.run(command2, capture_output=True))

    def _create_R_file(self):
        self.logger.write_line("Generate R.java")
        command = [f'{self.context["tools"]["aapt"]}', "package",
                   "-v", "-f", "-m",
                   "-S", f'{self.workspace}/res',
                   "-J", f'{self.workspace}/src',
                   "-M", f'{self.workspace}/AndroidManifest.xml',
                   "-I", f'{self.workspace}']
        self._execute_command(command)

    def _compile_code(self):
        self.logger.write_line("Compile java files")
        command = [f'{self.context["tools"]["javac"]}', "-verbose",
                   "-d", f'{self.workspace}/obj',
                   "-classpath", f'{self.context["tools"]["android.jar"]};{self.workspace}/obj',
                   "-sourcepath", f'{self.workspace}/src',
                   f'{self.workspace}/src/com/dochen/package1/*.java']
        self._execute_command(command)

    def _create_dex_file(self):
        self.logger.write_line("Generate dex file")
        command = [f'{self.context["tools"]["dx"]}',
                   "--dex", "--verbose",
                   f'--output={self.workspace}/bin/classes.dex',
                   f'{self.workspace}/obj',
                   f'{self.workspace}/lib']
        self._execute_command(command)

    def _create_unsigned_apk_file(self):
        self.logger.write_line("Generate unsigned apk file")
        command = [f'{self.context["tools"]["aapt"]}', "package",
                   "-v", "-f",
                   "-M", f'{self.workspace}/AndroidManifest.xml',
                   "-S", f'{self.workspace}/res',
                   "-I", f'{self.context["tools"]["android.jar"]}',
                   "-F", f"{self.workspace}/bin/AndroidTest.unsigned.apk",
                   f'{self.workspace}/bin']
        self._execute_command(command)
        
    def _sign_apk_file(self):
        self.logger.write_line("sign apk file")
        command = [f'{self.context["tools"]["jarsigner"]}', "-verbose",
                   "-keystore", f"{self.workspace}/AndroidTest.keystore",
                   "-storepass", "password",
                   "-keypass", "password",
                   "-signedjar", f"{self.workspace}/bin/AndroidTest.signed.apk",
                   f"{self.workspace}/bin/AndroidTest.unsigned.apk",
                   "AndroidTestKey"]
        self._execute_command(command)

    def _zipalign_apk_file(self):
        self.logger.write_line("zipalign apk file")
        command = [f'{self.context["tools"]["zipalign"]}',
                   "-v", "-f", "4",
                   f"{self.workspace}/bin/AndroidTest.signed.apk",
                   f"{self.workspace}/bin/AndroidTest.apk"]
        self._execute_command(command)