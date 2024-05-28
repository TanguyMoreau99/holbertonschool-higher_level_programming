#!/usr/bin/python3

"""
Module that defines a class Student.
"""


class Student:
    """
    A class that defines a student by:
    - Public instance attributes: first_name, last_name, age
    - Instantiation with first_name, last_name and age
    - Public method to_json that retrieves a dictionary representation
      of a Student instance
    - Public method reload_from_json that replaces all attributes
      of the Student instance
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: self.__dict__[attr]
                    for attr in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary to update attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
