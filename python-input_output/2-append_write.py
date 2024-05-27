#!/usr/bin/python3

"""Module pour ajouter une chaîne de caractères à la fin d'un fichier texte."""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d'un fichier texte (UTF-8) et
    renvoie le nombre de caractères ajoutés.

    Args:
        filename (str): Le nom du fichier dans lequel écrire. Par
        défaut, il est défini comme une chaîne vide.
        text (str): Le texte à ajouter dans le fichier.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
