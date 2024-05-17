#!/usr/bin/python3


def to_subtract(subtract_tmp):

    to_sub = 0
    max_list = max(subtract_tmp)

    for n in subtract_tmp:
        if max_list > n:
            to_sub += n

    return max_list - to_sub


def roman_to_int(roman_string):

    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    available_keys = list(roman_values.keys())

    result = 0
    last_rom = 0
    subtract_tmp = [0]

    for char in roman_string:
        for r_num in available_keys:
            if r_num == char:
                if roman_values[char] <= last_rom:
                    result += to_subtract(subtract_tmp)
                    subtract_tmp = [roman_values[char]]
                else:
                    subtract_tmp.append(roman_values[char])

                last_rom = roman_values[char]

    result += to_subtract(subtract_tmp)

    return result
