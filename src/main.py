from apk_generator import ApkGenerator
import os


def get_developer_information():
    developer_info = {}
    developer_info["company"] = "CHEN DONG"
    developer_info["organize"] = "chen"
    developer_info["organizeUnit"] = "dong"
    developer_info["location"] = "hangzhou"
    developer_info["state"] = "zhejiang"
    developer_info["countryCode"] = "CN"
    return developer_info


def get_tools_information():
    java_home = os.environ.get("JAVA_HOME")
    android_home = os.environ.get("ANDROID_HOME")
    if java_home is None or android_home is None:
        raise Exception("JAVA_HOME is not configured or ANDROID_HOME is not configured")
    tools = {}
    tools["javac"] = os.path.join(java_home, "bin\\javac.exe")
    tools["keytool"] = os.path.join(java_home, "bin\\keytool.exe")
    tools["jarsigner"] = os.path.join(java_home, "bin\\jarsigner.exe")
    tools["javadoc"] = os.path.join(java_home, "bin\\javadoc.exe")
    tools["adb"] = os.path.join(android_home, "platform-tools\\adb.exe")
    tools["aapt"] = os.path.join(android_home, "build-tools\\28.0.3\\aapt.exe")
    tools["zipalign"] = os.path.join(android_home, "build-tools\\28.0.3\\zipalign.exe")
    tools["dx"] = os.path.join(android_home, "build-tools\\28.0.3\\dx.bat")
    tools["android.jar"] = os.path.join(android_home, "platforms\\android-28\\android.jar")
    for tool in tools:
        if not os.path.isfile(tools[tool]):
            raise Exception(f"Cannot find {tool}")
    return tools


if __name__ == "__main__":
    context = {}
    context["tools"] = get_tools_information()
    context["project"] = {}
    context["developer"] = get_developer_information()
    ApkGenerator(context).run()
