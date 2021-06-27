# function to fill the total binary nummbers if user gives input of binary numbers less than 8 digits
def fillBinary(value):
    binary = str(value)
    if(len(binary) != 8):
        for i in range(len(binary),8):
            binary = "0" + binary
    else:
        binary = binary
    return binary

# function to fill the total binary nummbers if user gives input of decimal numbers less than 3 digits
def fillDecimal(value):
    decimal = str(value)
    if(len(decimal) != 3):
        for i in range(len(decimal),3):
            decimal = "0" + decimal
    else:
        decimal = decimal
    return decimal

# function to convert decimal number to binary number
def decimalToBin(num):
    value = ""
    while (num !=0):
        value = str(num%2) + value
        num = num//2
    BinaryVal = fillBinary(value)
    return BinaryVal

# function to convert binary number to decimal number
def binaryToDec(num):
    value = 0
    inc = 0
    while(num !=0):
        dec = num % 10
        value += dec* 2**inc
        num = num//10
        inc += 1
    DecimalVal = fillDecimal(value)
    return DecimalVal