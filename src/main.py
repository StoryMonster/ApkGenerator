from apk_generator import ApkGenerator
import xml.etree.ElementTree as ET
import sys


def read_item(parent, item_name):
    item = parent.find(item_name)
    return item.text if item is not None else ""


def get_developer_information(root):
    developer = root.find("developer")
    result = {}
    if developer is None: return result
    result["company"] = read_item(developer, "company")
    result["organize"] = read_item(developer, "organize")
    result["organizeUnit"] = read_item(developer, "organizeUnit")
    result["location"] = read_item(developer, "location")
    result["state"] = read_item(developer, "state")
    result["countryCode"] = read_item(developer, "countryCode")
    return result


def get_tools_information(root):
    tools = root.find("tools")
    result = {}
    if tools is None: return result
    result["javac"] = read_item(tools, "javac")
    result["keytool"] = read_item(tools, "keytool")
    result["jarsigner"] = read_item(tools, "jarsigner")
    result["javadoc"] = read_item(tools, "javadoc")
    result["adb"] = read_item(tools, "adb")
    result["aapt"] = read_item(tools, "aapt")
    result["zipalign"] = read_item(tools, "zipalign")
    result["dx"] = read_item(tools, "dx")
    result["android.jar"] = read_item(tools, "android.jar")
    return result


def read_config_file(file_name):
    context = {}
    tree = ET.parse(file_name)
    root = tree.getroot()
    context["tools"] = get_tools_information(root)
    context["project"] = {}
    context["developer"] = get_developer_information(root)
    return context


if __name__ == "__main__":
    context = read_config_file(sys.argv[1])
    ApkGenerator(context).run()