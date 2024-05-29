#!/usr/bin/python3
"""
Module de sérialisation basique qui ajoute la fonctionnalité de sérialiser
un dictionnaire Python dans un fichier JSON et de désérialiser le fichier JSON
pour recréer le dictionnaire Python.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON.

    Arguments:
        data (dict): Un dictionnaire Python avec des données.
        filename (str): Le nom du fichier de sortie au format JSON.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Charge 1fichier JSON et désérialise les données pour recréer un dict Python

    Arguments:
        filename (str): Le nom du fichier JSON d'entrée.

    Retourne:
        dict: Un dictionnaire Python avec les données JSON désérialisées
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
