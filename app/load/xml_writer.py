from typing import List, Dict
import xml.etree.ElementTree as ET


def write_xml(file_path: str, data: List[Dict]) -> None:
    root = ET.Element("addresses")
    for addr in data:
        address_el = ET.SubElement(root, "address")
        for key, value in addr.items():
            child = ET.SubElement(address_el, key)
            child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
