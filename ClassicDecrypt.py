import itertools
import string
import math
import os


class ClassicDecrypt:

    def __init__(self):
        pass

    def ceasarCipherDec(self, encStr, key):
        try:
            if not isinstance(encStr, str):
                raise TypeError("String is not passed to the function.")
            if not isinstance(key, int):
                raise TypeError("Key must be of integer type.")
        except Exception as e:
            print(e)
            return

        charList = "abcdefghijklmnopqrstuvwxyz"
        orgStr = ""

        for char in encStr:
            if char.isalpha():
                shift = (charList.index(char.lower()) - key) % len(charList)
                orgStr += charList[shift].upper()
            else:
                orgStr += char.upper()
        return orgStr

    def monoAlphaDec(self, encStr):
        try:
            if not isinstance(encStr, str):
                raise TypeError('Input is not a string.')
        except Exception as e:
            print(e)
            return None

        charFreq = "etaoinshrdlcumwfgypbvkjxqz"
        encStr = encStr.lower()
        orgStr = ""

        for char in encStr:
            if char.isalpha():
                index = charFreq.index(char)
                orgStr += chr(index + ord('a'))
            else:
                orgStr += char
        return orgStr

    def holdSeq(self, seq, size):
        it = iter(seq)
        while True:
            chunk = tuple(itertools.islice(it, size))
            if not chunk:
                return
            yield chunk

    def prepInput(self, orgStr):
        orgStr = "".join([char.upper()
                         for char in orgStr if char in string.ascii_letters])
        updStr = ""

        if len(orgStr) < 2:
            return orgStr

        for i in range(len(orgStr) - 1):
            updStr += orgStr[i]

            if orgStr[i] == orgStr[i + 1]:
                updStr += "X"

        updStr += orgStr[-1]

        if len(updStr) % 2 != 0:
            updStr += "X"
        return updStr

    def prepTable(self, key):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        table = []

        for char in key.upper():
            if char not in table and char in alpha:
                table.append(char)

        for char in alpha:
            if char not in table:
                table.append(char)
        return table

    def playfairDec(self, encStr, key):
        try:
            if not isinstance(encStr, str) or not isinstance(key, str):
                raise TypeError("Input must be of string type.")
        except Exception as e:
            print(e)
            return 0

        table = self.prepTable(key)
        encStr = self.prepInput(encStr)
        orgStr = ""

        for char1, char2 in self.holdSeq(encStr, 2):
            row1, col1 = divmod(table.index(char1), 5)
            row2, col2 = divmod(table.index(char2), 5)

            if row1 == row2:
                orgStr += table[row1 * 5 + (col1 - 1) % 5]
                orgStr += table[row2 * 5 + (col2 - 1) % 5]
            elif col1 == col2:
                orgStr += table[((row1 - 1) % 5) * 5 + col1]
                orgStr += table[((row2 - 1) % 5) * 5 + col2]
            else:
                orgStr += table[row1 * 5 + col2]
                orgStr += table[row2 * 5 + col1]
        return orgStr

    def railFenceDec(self, encStr, key):
        try:
            if not isinstance(encStr, str):
                raise TypeError("Input must be a string.")
            if not isinstance(key, int):
                raise TypeError("Input must be an integer.")

            if key <= 0:
                raise ValueError("Height of Grid can't be negetive or zero.")
        except Exception as e:
            print(e)
            return 0

        if key == 1:
            return encStr

        low = key - 1
        temp_grid = [[] for char in range(key)]
        grid = []

        for index in range(len(encStr)):
            num = index % (low * 2)
            num = min(num, low * 2 - num)
            temp_grid[num].append("*")

        count = 0
        for row in temp_grid:
            split = encStr[count: count + len(row)]
            grid.append(list(split))
            count += len(row)

        orgStr = ""
        for index in range(len(encStr)):
            num = index % (low * 2)
            num = min(num, low * 2 - num)
            orgStr += grid[num][0]
            grid[num].pop(0)

        return orgStr

    def columnarTpDec(self, encStr, key):
        try:
            if not isinstance(encStr, str) or not isinstance(key, str):
                raise TypeError('Input type must be string.')
        except Exception as e:
            print(e)
            return ' '

        cols = len(key)
        rows = int(math.ceil(len(encStr) / cols))
        strLst = list(encStr)
        keyLst = sorted(list(key))

        orgStrLst = []
        for char in range(rows):
            orgStrLst += [[None] * cols]

        count = 0
        counter = 0
        for char in range(cols):
            index = key.index(keyLst[count])

            for j in range(rows):
                orgStrLst[j][index] = strLst[counter]
                counter += 1
            count += 1

        orgStr = ""
        try:
            orgStr = ''.join(sum(orgStrLst, []))
        except Exception as e:
            print(e)

        nullCount = orgStr.count('_')
        if nullCount > 0:
            return orgStr[: -nullCount]
        return orgStr
