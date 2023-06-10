#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        j = ord(i)
        if j >= 97 and j <= 123:
            j = j - 32
        result += chr(j)
        print("{}".format(result))
