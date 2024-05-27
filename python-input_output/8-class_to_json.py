#!/usr/bin/python3

def class_to_json(obj):
    """
    Renvoie le dictionnaire de l'objet `obj` qui peut être facilement
    sérialisé en JSON.

    Args:
        obj: L'objet dont on veut obtenir le dictionnaire de l'attribut.

    Returns:
        dict: Un dictionnaire contenant tous les attributs de l'objet `obj`.
    """
    
    # Utilise la fonction `vars` pour obtenir le dictionnaire __dict__ de l'objet `obj`.
    # __dict__ est un attribut spécial qui contient tous les attributs de l'objet sous forme de dictionnaire.
    json_obj = vars(obj)
    
    # Retourne le dictionnaire obtenu
    return json_obj
