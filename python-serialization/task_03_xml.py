#!/usr/bin/python3
"""
Explore serialization and deserialization using
XML as an alternative format to JSON.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize the dictionary into XML format and save it to the given filename.

    :param dictionary: The Python dictionary to serialize
    :type dictionary: dict
    :param filename: The filename to save the serialized XML data
    :type filename: str
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)

    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from the given filename into a Python dictionary.

    :param filename: The filename containing the serialized XML data
    :type filename: str
    :return: The deserialized data as a Python dictionary
    :rtype: dict
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_data = {}

        for child in root:
            deserialized_data[child.tag] = child.text

        return deserialized_data

    except Exception as e:
        print("Error: {}".format(e))
        return None
