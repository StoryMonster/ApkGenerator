import xml.etree.ElementTree as ET


class XMLWriter(object):
    def __init__(self, filename):
        self.filename = filename

    def write(self, xml_struct):
        ET.ElementTree(xml_struct.getRoot()).write(self.filename, encoding="gbk", xml_declaration=True)
