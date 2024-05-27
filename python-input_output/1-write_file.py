#!/usr/bin/python3

"""Module pour écrire dans un fichier texte."""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (UTF-8) et
    renvoie le nombre de caractères écrits.

    Args:
        filename (str): Le nom du fichier dans lequel écrire. Par
        défaut, il est défini comme une chaîne vide.
        text (str): Le texte à écrire dans le fichier.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
