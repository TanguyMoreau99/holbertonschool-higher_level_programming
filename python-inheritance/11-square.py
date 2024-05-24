#!/usr/bin/python3
"""
11-square.py

This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The 'Square' class inherits from 'Rectangle'.
    """

    def __init__(self, size):
        """
        Initializes the Square with size, validated by BaseGeometry.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
