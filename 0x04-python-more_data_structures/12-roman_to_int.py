#!/usr/bin/python3

def get_value(str):
    rom_table = [
        {"M": 1000, "CM": 900},
        {"D": 500, "CD": 400},
        {"C": 100, "XC": 90},
        {"L": 50, "XL": 40},
        {"X": 10, "IX": 9},
        {"V": 5, "IV": 4},
        {"I": 1}
    ]
    for row in rom_table:
        if str in row:
            return row[str]
    return -1


def roman_to_int(roman_string):
    if roman_string is None:
        return 0

    stat = None
    result = 0

    for i in range(len(roman_string)):
        if (stat := get_value(roman_string[i:i+2])) != -1:
            result = result + stat
            continue
        if (stat := get_value(roman_string[i])) != -1:
            result = result + stat
            continue
        else:
            print("No value for {}".format(roman_string[i]))
            quit()
    return result
