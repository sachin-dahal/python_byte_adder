
# function to check whether a binary number input consists of valid binary numbers (0 and 1) or not
def checkBinary(num):
    valid = False
    val = str(num)
    for i in range(len(val)):
        if(val[i] == "0" or val[i] == "1"):
            valid = True
        else:
            print("\t|--------------------------------------------------------------|")
            print("\t|                        INVALID ATTEMPT!                      |")
            print("\t|         The number should consists only '0' and '1'.         |")
            print("\t|--------------------------------------------------------------|\n")
            valid = False
            break
    return valid

# function to check whether a number exceeds 8 digits or not
def binaryCrossover(num):
    valid = False
    if (num > 11111111):
        print("\t|--------------------------------------------------------------|")
        print("\t|                        INVALID ATTEMPT!                      |")
        print("\t|              The number is exceeding 11111111.               |")
        print("\t|         Please, enter the value which ranges upto 8 bits.    |")
        print("\t|--------------------------------------------------------------|\n")
        valid = False
    else:
        valid = True
    return valid


# functin to check whether a number exceeds 255 or not
def decimalCrossover(num):
    valid = False
    if (num > 255):
        print("\t|--------------------------------------------------------------|")
        print("\t|                        INVALID ATTEMPT!                      |")
        print("\t|                 The number is exceeding 255.                 |")
        print("\t|         Please, enter the value which ranges upto 255.       |")
        print("\t|--------------------------------------------------------------|\n")
        valid = False
    elif (num < 0):
        print("\t|--------------------------------------------------------------|")
        print("\t|                        INVALID ATTEMPT!                      |")
        print("\t|                   The number is less than 0.                 |")
        print("\t|         Please, enter the value which ranges upto 255.       |")
        print("\t|--------------------------------------------------------------|\n")
        valid = False
    else:
        valid = True
    return valid