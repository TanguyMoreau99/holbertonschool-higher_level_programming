#!/usr/bin/python3

"""
Fonction qui renvoie un objet (structure de données Python)
représenté par une chaîne JSON.
"""

import json


def from_json_string(my_str):
    """
    Fonction qui renvoie un objet (structure de données Python)
    représenté par une chaîne JSON.

    Args:
        my_str: La chaîne de caractères JSON à convertir en objet Python.
    """
    return json.loads(my_str)
