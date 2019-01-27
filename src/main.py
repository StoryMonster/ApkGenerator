from apk_generator import ApkGenerator
import xml.etree.ElementTree as ET
import sys


def get_tool_path(tools, tool_name):
    tool = tools.find(tool_name)
    return tool.text if tool is not None else ""

def read_config_file(file_name):
    context = {}
    tree = ET.parse(file_name)
    root = tree.getroot()
    tools = root.find("tools")
    if tools is not None:
        context["tools"] = {}
        context["tools"]["javac"] = get_tool_path(tools, "javac")
        context["tools"]["keytool"] = get_tool_path(tools, "keytool")
        context["tools"]["jarsigner"] = get_tool_path(tools, "jarsigner")
        context["tools"]["javadoc"] = get_tool_path(tools, "javadoc")
        context["tools"]["adb"] = get_tool_path(tools, "adb")
        context["tools"]["aapt"] = get_tool_path(tools, "aapt")
        context["tools"]["zipalign"] = get_tool_path(tools, "zipalign")
        context["tools"]["dx"] = get_tool_path(tools, "dx")
        context["tools"]["android.jar"] = get_tool_path(tools, "android.jar")
    context["project"] = {}
    context["position"] = {}
    return context


if __name__ == "__main__":
    context = read_config_file(sys.argv[1])
    generator = ApkGenerator(context)
    generator.main_window.mainloop()