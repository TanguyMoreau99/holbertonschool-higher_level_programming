#!/usr/bin/python3

"""
Fonction qui renvoie la représentation JSON d'un
objet (chaîne de caractères).
"""

import json


def to_json_string(my_obj):
    """
    Fonction qui renvoie la représentation JSON d'un
    objet (chaîne de caractères).

    Args:
        my_obj: L'objet à convertir en format JSON.
    """
    return json.dumps(my_obj)
