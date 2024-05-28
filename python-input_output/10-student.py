#!/usr/bin/python3

"""
Module qui définit une classe Student.
"""


class Student:
    """
    Une classe qui définit un étudiant avec :
    - Attributs d'instance publics : first_name, last_name, age
    - Initialisation avec first_name, last_name et age
    - Méthode publique to_json qui récupère une représentation
      sous forme de dictionnaire d'une instance Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de Student.

        Args:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Récupère une représentation sous forme de dictionnaire
        d'une instance de Student.

        Args:
            attrs (list): Une liste de noms d'attributs à récupérer.
                          Si None, retourne tous les attributs.

        Returns:
            dict: La représentation sous forme de dictionnaire de l'instance Student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: self.__dict__[attr]
                    for attr in attrs if attr in self.__dict__}
