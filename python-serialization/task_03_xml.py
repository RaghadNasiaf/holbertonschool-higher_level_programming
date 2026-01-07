#!/usr/bin/env python3
"""
Module for serializing and deserializing dictionaries using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    Args:
        dictionary (dict): The data to serialize.
        filename (str): The name of the file to save to.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
        
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.
    Args:
        filename (str): The name of the XML file.
    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct dictionary from XML child elements
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
