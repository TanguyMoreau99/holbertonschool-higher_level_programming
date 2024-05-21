#!/usr/bin/python3
"""
Module 2-matrix_divided
Ce module fournit une fonction `matrix_divided` pour diviser tous les éléments d'une matrice par un diviseur.
"""

def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur et retourne une nouvelle matrice.
    
    Args:
        matrix (list of lists of int/float): La matrice à diviser.
        div (int/float): Le diviseur.

    Returns:
        list of lists of float: Une nouvelle matrice avec les éléments divisés par div, arrondis à 2 décimales.

    Raises:
        TypeError: Si la matrice n'est pas une liste de listes d'entiers ou de flottants,
                   ou si les lignes de la matrice n'ont pas la même taille,
                   ou si le diviseur n'est pas un nombre.
        ZeroDivisionError: Si le diviseur est égal à 0.
    """
    # Vérification de la matrice
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification du diviseur
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Division des éléments de la matrice
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    
    return new_matrix
