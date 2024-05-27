#!/usr/bin/python3

"""Module pour lire un fichier texte."""


def read_file(filename=""):
    """
    Lit un fichier texte (UTF-8) et l'affiche sur stdout.

    Args:
        filename (str): Le nom du fichier à lire. Par défaut, il est
        défini comme une chaîne vide.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

