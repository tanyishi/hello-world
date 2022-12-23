from xml.etree import ElementTree as ET
tree = ET.parse('data-text.xml')
root = tree.getroot()
print dir(root)