import xml.etree.ElementTree as ET

tree = ET.parse('config.xml')
root = tree.getroot()
print(root.tag)
compile_node = root.find("compile")

print(compile_node[0].text)