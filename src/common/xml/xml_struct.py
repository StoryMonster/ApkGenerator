import xml.etree.ElementTree as ET

class XMLStruct(object):
    def __init__(self, rootname):
        self.root = ET.Element(rootname)

    def addTextSubElement(self, name, text, attrs={}):
        node = ET.SubElement(self.root, name, attrib=attrs)
        node.text = text
        node.tail = "\n"

    def getRoot(self):
        return self.root
