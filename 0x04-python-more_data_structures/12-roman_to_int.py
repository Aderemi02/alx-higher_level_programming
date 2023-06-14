#!/usr/bin/python3
def minus(finalist):
    tot = 0
    newlst = max(finalist)
    for i in finalist:
        if newlst > i:
            tot += i
    return (newlst - tot)


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_list = list(rom_num.keys())
    rand = 0
    count = 0
    finalist = [0]

    for rom in roman_string:
        for num in rom_list:
            if num == rom:
                if rom_num.get(rom) <= rand:
                    count += minus(finalist)
                    finalist = [rom_num.get(rom)]
                else:
                    finalist.append(rom_num.get(rom))
                finalist = rom_num.get(rom)
    count += minus(finalist)
    return (count)
