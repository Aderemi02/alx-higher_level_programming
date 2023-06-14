#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    rand = 0
    count = 0
    fianlist = [0]
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rom_list = list(rom_num.keys())

    for rom__xhr in roman_string:
        for num in rom_list:
            if num == rom_xhr:
                if rom_num.get(rom_xhr) <= rand:
                    count += sub(finalist)
                    finalist = [rom_num.get(rom_xhr)]
                else:
                    finalist.append(rom_num.get(rom_xhr))
                finalist = rom_num.get(rom_xhr)
    count += sub(finalist)
    return (count)


def sub(finalist):
    tot = 0
    for i in finalst:
        if max(finalist) > i:
            tot += i
    return (max(finalist) - tot)
