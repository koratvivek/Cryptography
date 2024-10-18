import numpy as np
import string
import os


class SymmatricDecrypt:

    def __init__(self):
        pass

    def trnsStr(self, orgStr, key, mode):
        alpha = "abcdefghijklmnopqrstuvwxyz"

        try:
            if not isinstance(orgStr, str) or not isinstance(key, str) or not isinstance(mode, str):
                raise TypeError("Input type should be string.")
        except Exception as e:
            print(e)
            return None

        updated = []
        count = 0

        for char in orgStr:
            num = alpha.find(char.lower())
            if num != -1:
                if mode == 'encrypt':
                    num += alpha.find(key[count % len(key)])
                elif mode == 'decrypt':
                    num -= alpha.find(key[count % len(key)])

                num %= len(alpha)

                if char.islower():
                    updated.append(alpha[num].upper())
                elif char.isupper():
                    updated.append(alpha[num])

                count = (count + 1) % len(key)

            else:
                updated.append(char)
        return "".join(updated)

    def vigenereDec(self, orgStr, key):
        try:
            if not isinstance(orgStr, str) or not isinstance(key, str):
                raise TypeError('Input type should be string.')
        except Exception as e:
            print(e)
            return None
        return self.trnsStr(orgStr, key, "decrypt")

    def charToNum(self, char):
        table = [
            ["a", "b", "c", "d", "e"],
            ["f", "g", "h", "i", "k"],
            ["l", "m", "n", "o", "p"],
            ["q", "r", "s", "t", "u"],
            ["v", "w", "x", "y", "z"],
        ]
        table = np.array(table)
        index1, index2 = np.where(char == table)
        num = np.concatenate([index1 + 1, index2 + 1])
        return num

    def numToChar(self, index1, index2):
        table = [
            ["a", "b", "c", "d", "e"],
            ["f", "g", "h", "i", "k"],
            ["l", "m", "n", "o", "p"],
            ["q", "r", "s", "t", "u"],
            ["v", "w", "x", "y", "z"],
        ]
        table = np.array(table)
        return table[index1 - 1, index2 - 1]

    def polybiusDec(self, encStr):
        try:
            if not isinstance(encStr, str):
                raise TypeError("Input type must be string.")
        except Exception as e:
            print(e)
            return None
        encStr = encStr.lower()

        orgStr = ""
        for index in range(int(len(encStr) / 2)):
            if encStr[index * 2] != " ":
                index1 = encStr[index * 2]
                index2 = encStr[index * 2 + 1]

                char = self.numToChar(int(index1), int(index2))
                orgStr += char
            elif encStr[index * 2] == " ":
                orgStr += " "
        return orgStr

    def generateTable(self, key):
        table = {
            "A": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
            "B": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
            "C": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
            "D": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
            "E": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
            "F": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
            "G": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
            "H": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
            "I": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
            "J": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
            "K": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
            "L": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
            "M": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
            "N": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
            "O": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
            "P": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
            "Q": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
            "R": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
            "S": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
            "T": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
            "U": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
            "V": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
            "W": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
            "X": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
            "Y": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
            "Z": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
        }
        return [table[char] for char in key.upper()]

    def portaDec(self, encStr, key):
        try:
            if not isinstance(encStr, str) or not isinstance(key, str):
                raise TypeError("Input type must be string.")
        except Exception as e:
            print(e)
            return None
        orgStr = ""
        count = 0
        table = self.generateTable(key)

        for char in encStr.upper():
            if char.isalpha():
                row = 0 if char in table[count][0] else 1
                col = table[count][row].index(char.upper())
                sec_row = 1 - row
                sec_char = table[count][sec_row][col]
                orgStr += sec_char
                count = (count + 1) % len(table)
            else:
                orgStr += char
        return orgStr

  