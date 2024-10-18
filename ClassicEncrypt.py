import itertools
import string
import math
import os


class ClassicEncrypt:

    def __init__(self):
        pass

    def ceasarCipherEnc(self, orgStr, key):
        try:
            if not isinstance(orgStr, str):
                raise TypeError("String is not passed to the function.")
            if not isinstance(key, int):
                raise TypeError('Key must be of integer type.')
        except Exception as e:
            print(e)
            return

        charList = "abcdefghijklmnopqrstuvwxyz"
        encStr = ""

        for char in orgStr:
            if char.isalpha():
                shift = (charList.index(char.lower()) + key) % len(charList)
                encStr += charList[shift].upper()
            else:
                encStr += char.upper()
        return encStr

    def monoAlphaEnc(self, orgStr):
        try:
            if not isinstance(orgStr, str):
                raise TypeError('Input is not a string.')
        except Exception as e:
            print(e)
            return None

        charFreq = "etaoinshrdlcumwfgypbvkjxqz"
        orgStr = orgStr.lower()
        encStr = ""

        for char in orgStr:
            if char.isalpha():
                index = ord(char) - ord('a')
                encStr += charFreq[index].upper()
            else:
                encStr += char.upper()
        return encStr

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

    def playfairEnc(self, orgStr, key):
        try:
            if not isinstance(orgStr, str) or not isinstance(key, str):
                raise TypeError("Input must be of string type.")
        except Exception as e:
            print(e)
            return 0

        table = self.prepTable(key)
        orgStr = self.prepInput(orgStr)
        encStr = ""

        for char1, char2 in self.holdSeq(orgStr, 2):
            row1, col1 = divmod(table.index(char1), 5)
            row2, col2 = divmod(table.index(char2), 5)

            if row1 == row2:
                encStr += table[row1 * 5 + (col1 + 1) % 5]
                encStr += table[row2 * 5 + (col2 + 1) % 5]
            elif col1 == col2:
                encStr += table[((row1 + 1) % 5) * 5 + col1]
                encStr += table[((row2 + 1) % 5) * 5 + col2]
            else:
                encStr += table[row1 * 5 + col2]
                encStr += table[row2 * 5 + col1]

        return encStr

    def railFenceEnc(self, orgStr, key):
        try:
            if not isinstance(orgStr, str):
                raise TypeError("Input must be a string.")
            if not isinstance(key, int):
                raise TypeError("Input must be an integer.")

            if key <= 0:
                raise ValueError("Height of Grid can't be negetive or zero.")
        except Exception as e:
            print(e)
            return 0

        if key == 1 or len(orgStr) <= key:
            return orgStr

        temp_grid = [[] for char in range(key)]
        low = key - 1

        for index, char in enumerate(orgStr):
            num = index % (low * 2)
            num = min(num, low * 2 - num)
            temp_grid[num].append(char)

        grid = ["".join(row) for row in temp_grid]
        encStr = "".join(grid)

        return encStr

    def columnarTpEnc(self, orgStr, key):
        try:
            if not isinstance(orgStr, str) or not isinstance(key, str):
                raise TypeError("Input type must be string.")
        except Exception as e:
            print(e)
            return None

        cols = len(key)
        rows = int(math.ceil(len(orgStr) / cols))
        strLst = list(orgStr)
        keyLst = sorted(list(key))

        padd = int((rows * cols) - len(orgStr))
        strLst.extend("_"*padd)

        matrix = [strLst[i: i+cols] for i in range(0, len(strLst), cols)]

        count = 0
        encStr = ""
        for char in range(cols):
            index = key.index(keyLst[count])
            encStr += ''.join([row[index] for row in matrix])
            count += 1
        return encStr