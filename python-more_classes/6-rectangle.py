#!/usr/bin/python3
"""
Module 6-rectangle
Ce module fournit une classe `Rectangle` qui définit un rectangle
avec des attributs privés pour la largeur et la hauteur,ainsi que
des méthodes pour calculer l'aire, le périmètre et des représentations
sous forme de chaîne de caractères.
"""


class Rectangle:
    """
    Classe qui définit un rectangle par :
    - des attributs privés pour la largeur (width) et la hauteur (height)
    - des propriétés pour accéder et modifier ces attributs avec des
      vérifications
    - des méthodes pour calculer l'aire (area), le périmètre (perimeter)
    - des méthodes pour afficher le rectangle en utilisant `print()`,
      `str()` et `repr()`
    - une méthode pour afficher un message lors de la suppression de l'objet
    - un attribut de classe pour suivre le nombre d'instances de la classe
    """

    # Attribut de classe
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialisation des attributs width et height, et incremente
          number_of_instances"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Récupère la largeur du rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle
        Vérifie que la valeur est un entier et qu'elle est positive
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle
        Vérifie que la valeur est un entier et qu'elle est positive
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le rectangle avec le
        caractère #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Retourne une chaîne de caractères représentant l'objet Rectangle
        Permet de recréer l'objet en utilisant eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Affiche un message lors de la suppression de l'objet Rectangle et
        décrémente number_of_instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
