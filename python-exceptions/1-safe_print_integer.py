#!/usr/bin/python3


def safe_print_integer(value):
    """
    Attempts to print the provided value as an integer.

    Args:
        value (any): The value to be printed as an integer.

    Returns:

    """
    try:
        # Try to format and print the value as an integer
        print("{:d}".format(value))
        # If successful, return True
        return True
    except ValueError:
        # Handle the case where the value cannot be formatted as an integer
        return False
    except TypeError:

        return False
