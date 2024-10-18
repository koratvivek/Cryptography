from Conversion import *
from ClassicEncrypt import *
from ClassicDecrypt import *
from SymmatricEncrypt import *
from SymmatricDecrypt import *


class Main:

    conv = Conversion()
    clEnc = ClassicEncrypt()
    clDec = ClassicDecrypt()
    sEnc = SymmatricEncrypt()
    sDec = SymmatricDecrypt()

    def __init__(self):
        pass

    def main(self):
        print("Welcome to the CryptoBuzz.")
        print("A hub based on cryptography")

        while True:
            print()
            print()
            print("Enter the choice : ")
            print("1. For Data Conversion ")
            print("2. For Classical Encryption")
            print("3. For Symmatric Encryption")
            print("4. To Quit")
            inp = input("")
            print()
            if inp == '1':
                print("Enter the conversion Type : ")
                print("1. Binary To Decimal")
                print("2. Binary To Octal")
                print("3. Decimal To Binary")
                print("4. Decimal To Octal")
                print("5. Octal To Binary")
                print("6. Octal To Decimal")
                choice = input('')
                print()

                if choice == '1':
                    binary = input("Enter the Binary number : ")
                    decimal = self.conv.binToDec(binary)
                    print("Decimal Number : ", decimal)
                    print()
                elif choice == '2':
                    binary = input("Enter the Binary number : ")
                    octal = self.conv.binToOctal(binary)
                    print("Decimal Number : ", octal)
                    print()
                elif choice == '3':
                    num = input("Enter the Number : ")
                    if not num.isdigit():
                        print('Entered String is not a number.')
                    else:
                        binary = self.conv.decToBin(int(num))
                        print("Converted Binary number : ", binary)
                        print()
                elif choice == '4':
                    num = input("Enter the Number : ")
                    if not num.isdigit():
                        print("Entered String is not a number.")
                    else:
                        octal = self.conv.decToOct(int(num))
                        print("Converted Octal Number : ", octal)
                        print()
                elif choice == '5':
                    octal = input("Enter the Octal number : ")
                    binary = self.conv.octToBin(octal)
                    print(f"Binary number : {binary}")
                    print()
                elif choice == '6':
                    octal = input("Enter the Octal number : ")
                    decimal = self.conv.octToDec(octal)
                    print(f"Decimal number : {decimal}")
                    print()
                else:
                    print("Enter a valid Choice.")
                    print()

            elif inp == '2':
                print("Enter the Encryption Type : ")
                print("1. Ceasar Cipher")
                print("2. Mono Alphabetic Cipher")
                print("3. PlayFair Cipher")
                print("4. Rail Fence Encryption")
                print("5. Row Column Transposition")
                choice = input('')
                print()

                if choice == '1':
                    innerChoice = input("Enter 1. to Encrypt 2. to Decrypt")
                    if innerChoice == '1':
                        orgStr = input("Enter the string to be Encrypted : ")
                        key = input("Enter the key (integer value) :")
                        if not key.isdigit():
                            print('Please Enter a valid key.')
                        else:
                            encStr = self.clEnc.ceasarCipherEnc(
                                orgStr, int(key))
                            print(f"Encrypted String : {encStr}")
                    elif innerChoice == '2':
                        encStr = input("Enter the encrypted String : ")
                        key = input('Enter the key (integer value) :')
                        if not key.isdigit():
                            print("Please Enter a valid key.")
                        else:
                            orgStr = self.clDec.ceasarCipherDec(
                                encStr, int(key))
                            print(f"Original String : {orgStr}")
                    else:
                        print("Please Enter a valid choice.")
                elif choice == '2':
                    innerChoice = input("Enter 1. to Encrypt 2. to Decrypt")
                    if innerChoice == '1':
                        orgStr = input("Enter the string to be Encrypted : ")
                        encStr = self.clEnc.monoAlphaEnc(orgStr)
                        print(f"Encrypted String : {encStr}")
                    elif innerChoice == '2':
                        encStr = input("Enter the encrypted String : ")
                        orgStr = self.clDec.monoAlphaDec(encStr)
                        print(f"Original String : {orgStr}")
                    else:
                        print("Please Enter a valid choice.")

                elif choice == '3':
                    innerChoice = input("Enter 1. to Encrypt 2. to Decrypt : ")
                    if innerChoice == '1':
                        orgStr = input("Enter the string to be encrypted : ")
                        key = input("Enter the key : ")
                        encStr = self.clEnc.playfairEnc(orgStr, key)
                        print(f" Encrypted String : {encStr}")
                    elif innerChoice == '2':
                        encStr = input('Enter the encrypted string : ')
                        key = input('Enter the key : ')
                        orgStr = self.clDec.playfairDec(encStr, key)
                        print(f" Original String : {orgStr}")
                    else:
                        print('Please Enter a valid choice')

                elif choice == '4':
                    innerChoice = input("Enter 1. to Encrypt 2. to Decrypt")
                    if innerChoice == '1':
                        orgStr = input("Enter the string to be Encrypted : ")
                        key = input("Enter the key (integer value) :")
                        if not key.isdigit():
                            print('Please Enter a valid key.')
                        else:
                            encStr = self.clEnc.railFenceEnc(orgStr, int(key))
                            print(f"Encrypted String : {encStr}")
                    elif innerChoice == '2':
                        encStr = input("Enter the encrypted String : ")
                        key = input('Enter the key (integer value) :')
                        if not key.isdigit():
                            print("Please Enter a valid key.")
                        else:
                            orgStr = self.clDec.railFenceDec(encStr, int(key))
                            print(f"Original String : {orgStr}")
                    else:
                        print("Please Enter a valid choice.")

                elif choice == '5':
                    innerChoice = input("Enter 1. to Encrypt 2. to Decrypt : ")
                    if innerChoice == '1':
                        orgStr = input("Enter the string to be encrypted : ")
                        key = input("Enter the key : ")
                        encStr = self.clEnc.columnarTpEnc(orgStr, key)
                        print(f" Encrypted String : {encStr}")
                    elif innerChoice == '2':
                        encStr = input('Enter the encrypted string : ')
                        key = input('Enter the key : ')
                        orgStr = self.clDec.columnarTpDec(encStr, key)
                        print(f" Original String : {orgStr}")
                    else:
                        print('Please Enter a valid choice')

                else:
                    print("Enter the Valid Choice.")
                print()

            elif inp == '3':
                print("Enter the Encryption Type : ")
                print("1. Vigenere Cipher")
                print("2. Polybius Cipher")
                print("3. Porta Cipher")
                choice = input('')
                print()

                if choice == '1':

                    innerChoice = input('Enter 1. to Encrypt 2. to Decrypt : ')
                    if innerChoice == '1':
                        orgStr = input('Enter the string : ')
                        key = input('Enter the Key : ')
                        encStr = self.sEnc.vigenereEnc(orgStr, key)
                        print(f" Encrypted String : {encStr}")
                    elif innerChoice == '2':
                        encStr = input('Enter the encrypted string : ')
                        key = input('Enter the key : ')
                        orgStr = self.sDec.vigenereDec(encStr, key)
                        print(f" Original String : {orgStr}")
                    else:
                        print('Please Enter the valid choice.')

                elif choice == '2':
                    innerChoice = input('Enter 1. to Encrypt 2. to Decrypt : ')
                    if innerChoice == '1':
                        orgStr = input('Enter the string : ')
                        encStr = self.sEnc.polybiusEnc(orgStr)
                        print(f" Encrypted String : {encStr}")
                    elif innerChoice == '2':
                        encStr = input('Enter the encrypted string : ')
                        orgStr = self.sDec.polybiusDec(encStr)
                        print(f" Original String : {orgStr}")
                    else:
                        print('Please Enter the valid choice.')

                elif choice == '3':
                    innerChoice = input('Enter 1. to Encrypt 2. to Decrypt : ')
                    if innerChoice == '1':
                        orgStr = input('Enter the string : ')
                        key = input('Enter the Key : ')
                        encStr = self.sEnc.portaEnc(orgStr, key)
                        print(f" Encrypted String : {encStr}")
                    elif innerChoice == '2':
                        encStr = input('Enter the encrypted string : ')
                        key = input('Enter the key : ')
                        orgStr = self.sDec.portaDec(encStr, key)
                        print(f" Original String : {orgStr}")
                    else:
                        print('Please Enter the valid choice.')
                else:
                    print("Enter the Valid Choice.")
                print()

            elif inp == '4':
                print("You have successfully quitted the system.")
                break
            else:
                print("please enter a valid choice.")


obj = Main()
obj.main()
