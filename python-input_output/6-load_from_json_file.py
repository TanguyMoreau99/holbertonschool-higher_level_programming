#!/usr/bin/python3

"""
Créer des objets à partir d'un fichier JSON.
"""

import json


def load_from_json_file(filename):
    """
    Fonction pour créer un objet à partir d'un fichier JSON.

    Args:
        filename: Le nom du fichier.

    Returns:
        L'objet JSON contenu dans le fichier.
    """
    with open(filename, "r", encoding="utf-8") as file:
        json_object = json.load(file)
        return json_object
