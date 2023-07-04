#!/usr/bin/python3
"""writing a function that prints a text with 2 new lines
after each of these character: .,? and :
"""


def text_indentation(text):
    """a function to indent text with the argument:
    text as the parameter passed
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    num = 0
    while num < len(text) and text[num] == ' ':
        num += 1

    while num < len(text):
        print(text[num], end="")
        if text[num] in ".?:" or text[num] == "\n":
            if text[num] in ".:?":
                print("\n")
            num += 1
            while num < len(text) and text[num] == ' ':
                num += 1
            continue
        num += 1
