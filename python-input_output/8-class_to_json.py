#!/usr/bin/python3
"""
Module fournissant une fonction pour convertir les attributs d'un obj en un dic
"""


def class_to_json(obj):
    """
    Renvoie le dictionnaire de l'objet `obj` qui peut être facilement
    sérialisé en JSON.

    Args:
        obj: L'objet dont on veut obtenir le dictionnaire des attributs.

    Returns:
        dict: Un dictionnaire contenant tous les attributs de l'objet `obj`.
    """
    json_obj = vars(obj)
    return json_obj
