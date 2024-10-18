class Conversion:
    def checkNegBin(self,bin):
        if not isinstance(bin,str):
            raise TypeError('String is not passed as input.')
        if not bin:
            raise ValueError('Empty string has been passed.')
        neg = bin[0] == "-"
        bin = bin[1::]
        if not all(char in "01" for char in bin):
            raise ValueError('Entered String is not Binary.')
        return neg
    
    def binToDec(self,bin):
        neg = False
        try:
            neg = self.checkNegBin(bin)
        except Exception as e:
            print(e)
            return 0

        if neg:
            bin = bin[1::]
        dec = 0
        for char in bin:
            dec = 2 * dec + int(char)
        return -dec if neg else dec
    
    def binToHex(self,bin):
        neg = False
        try:
            neg = self.checkNegBin(bin)
        except Exception as e:
            print(e)
            return 0
        if neg:
            bin = bin[1::]

        bin_hex = {
            "0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "a",
            "1011": "b",
            "1100": "c",
            "1101": "d",
            "1110": "e",
            "1111": "f"
        }

        reqZeros = "0" * (((len(bin) - 1) // 4 + 1) * 4 - len(bin))
        bin = reqZeros + bin

        hex = ""

        for char in range(0, len(bin) , 4):
            hex += bin_hex[ bin[char : char + 4] ]
        return "-"+hex if neg else hex
    
    def binToOctal(self,bin):
        neg = False
        try:
            neg = self.checkNegBin(bin)
        except Exception as e:
            print(e)
            return 0

        if neg:
            bin = bin[1::]

        bin_oct = {
            "000": "0",
            "001": "1",
            "010": "2",
            "011": "3",
            "100": "4",
            "101": "5",
            "110": "6",
            "111": "7"
        }

        reqZeros = "0" * (((len(bin) - 1) // 3 + 1)*3 - len(bin))
        bin = reqZeros + bin
        oct = ""

        for index in range(0, len(bin) , 3):
            oct += bin_oct[ bin[index : index+3] ]
        return "-"+oct if neg else oct
    
    def checkNegDec(self,dec):
        if isinstance(dec,str):
            raise TypeError('str value has been passed to the function.')
        if isinstance(dec,float):
            raise TypeError('float value has been passed to the function.')

        neg = True if dec < 0 else False
        return neg
    
    def decToBin(self,dec):
        neg = False
        try:
            neg = self.checkNegDec(dec)
        except Exception as e:
            print(e)
            return 0
        
        dec = -dec if neg else dec
        if dec in [0,1]:
            return "-"+str(dec) if neg else str(dec)

        bin = ""
        while dec > 0:
            bin += str(dec % 2)
            dec //= 2
        bin = bin[::-1]
        return "-"+bin if neg else bin

    def decToOct(self,dec):
        neg = False
        try:
            neg = self.checkNegDec(dec)
        except Exception as e:
            print(e)
            return 0
        oct_list = [i for i in range(8)]

        dec = -dec if neg else dec
        if dec in oct_list:
            return "-"+str(dec) if neg else str(dec)
        
        oct = ""
        while dec > 0:
            oct += str(dec % 8)
            dec //= 8
        oct = oct[::-1]
        return "-"+oct if neg else oct

    def decToHex(self,dec):
        neg = False
        try:
            neg = self.checkNegDec(dec)
        except Exception as e:
            print(e)
            return 0

        dec = -dec if neg else dec
        
        hex_dict = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
        }
        hex = ""

        if dec in hex_dict:
            return "-"+hex_dict[dec] if neg else hex_dict[dec]

        while dec > 0:
            hex += hex_dict[dec % 16]
            dec //= 16
        hex = hex[::-1]
        return "-"+hex if neg else hex 

    def checkNegOct(self,oct):
        if not isinstance(oct,str):
            raise TypeError('String is not passed as input.')
        if not oct:
            raise ValueError('Empty string has been passed.')
        neg = oct[0] == "-"
        oct = oct[1::]
        oct_digits = "01234567"
        for digit in oct:
            if digit not in oct_digits:
                raise ValueError("Octal value has not been passed.")
        return neg    
    
    def octToBin(self,oct):
        neg = False
        try:
            neg = self.checkNegOct(oct)
        except Exception as e:
            print(e)
            return 0

        oct = oct[1::] if neg else oct
        if oct in ['0','1']:
            return "-"+oct if neg else oct
        
        oct_digits = "01234567"
        bin = ""
        for digit in oct:
            bin_val = ""
            val = int(digit)
            for value in range(3):
                bin_val = str(val % 2) + bin_val
                val //= 2
            bin += bin_val
        
        return "-"+bin if neg else bin
    
    def octToDec(self,oct):
        neg = False
        try:
            neg = self.checkNegOct(oct)
        except Exception as e:
            print(e)
            return 0
        
        oct = oct[1::] if neg else oct
        
        dec = 0
        for char in oct:
            dec = 8 * dec + int(char)
        
        return -dec if neg else dec
    
    def octToHex(self,oct):
        neg = False
        try:
            neg = self.checkNegOct(oct)
        except Exception as e:
            print(e)
            return 0
        
        dec = self.octToDec(oct)
        hex = self.decToHex(dec)
        return "-"+hex if neg else hex
    
    def checkNegHex(self,hex):
        if not isinstance(hex,str):
            raise TypeError('String is not passed as input.')
        if not hex:
            raise ValueError('No value was passed to the function.')
        neg = hex[0] == "-"
        hex_values = "0123456789ABCDEF"
        for digit in hex:
            if digit.upper() not in hex_values:
                raise ValueError("Hexa-decimal value has not been passed.")
        return neg
    
    def hexToBin(self,hex):
        neg = False
        try:
            neg = self.checkNegHex(hex)
        except Exception as e:
            print(e)
            return 0
        
        hex = hex[1:] if neg else hex
        bin = bin(int(hex, 16))[2:]

        # dec_num = int(hex,16)

        # while dec_num > 0:
        #     bin += str(dec_num % 2)
        #     dec_num //= 2
        # bin = bin[::-1]
        return "-"+bin if neg else bin
    
    def hexToDec(self,hex):
        neg = False
        try:
            neg = self.checkNegHex(hex)
        except Exception as e:
            print(e)
            return 0
        
        hex = hex[1::] if neg else hex
        dec = 0
        hex_table = {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "a" : 10,
            "b" : 11,
            "c" : 12,
            "d" : 13,
            "e" : 14,
            "f" : 15,
        }
        # hex_table = {hex(i)[2:]: i for i in range(16)}
        for char in hex:
            dec = 16 * dec + hex_table[char.lower()]
        return -dec if neg else dec
    
    def hexToOct(self,hex):
        neg = False
        try:
            neg = self.checkNegHex(hex)
        except Exception as e:
            print(e)
            return 0
        
        hex = hex[1:] if neg else hex
        bin = self.hexToBin(hex)
        oct = self.binToOctal(bin)
        return "-"+oct if neg else oct

