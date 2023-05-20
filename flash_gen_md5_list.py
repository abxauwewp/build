#!/usr/bin/env python
import os
import binascii
import xml.etree.cElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom

import hashlib
def md5sum(filename, blocksize=65536):
    h = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            h.update(block)
    return h.hexdigest()

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def gen_md5_xml():
	path = os.path.join(os.path.dirname(__file__), 'images')
	files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	xml = os.path.join(os.path.dirname(__file__), "md5sum.xml")

	root = ET.Element("root")
	digests = ET.SubElement(root, "digests")
	for file in files:
		file = os.path.join(path, file)
		digest = ET.SubElement(digests, "digest", name=os.path.basename(file), hash="md5")
		digest.text = md5sum(file)

	xml_str = prettify(root)

	with open(xml,"w") as f:
		f.write(xml_str)

#------------------------------------------------------------------------------
if __name__ == "__main__":
	gen_md5_xml()

