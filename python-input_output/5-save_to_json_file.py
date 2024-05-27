#!/usr/bin/python3

"""
Écrire un objet dans un fichier texte avec une représentation JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet dans un fichier texte avec une représentation JSON.

    Args:
        my_obj: L'objet à écrire dans le fichier.
        filename: Le nom du fichier.

    Returns:
        Le fichier texte avec la représentation JSON de l'objet.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
