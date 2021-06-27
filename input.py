from conversion import *
from adder import *
from validation import *

# Creating a function to take an input from the user
def inputNo():
    binList=[]
    flag = False
    while(not flag):
        # taking input from a user to enter in an specific conversion mode
        st = input("\nSelect the terms below...\nEnter [b] or [B] for Binary and [d] or [D] for decimal.\n")
        st_num=False

        # handling an exception to check whether an input from a user is integer
        try:
            st_num = isinstance(int(st),int)
        except:
            pass
        
        if(st.lower() == 'b'):
            # binary number conversion mode
            print("\t<^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^>")
            print("\t<  Conditions:                                         >")
            print("\t<------------------------------------------------------>")
            print("\t<  * Numbers should consists only 0 and 1.             >")
            print("\t<  * Numbers should be less than or equal to 8 digits. >")
            print("\t<  * Alphabets are not allowed.                        >")
            print("\t<                                                      >")
            print("\t<vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv>\n")

            while (not flag):
                try:
                    correctInput = False
                    while not correctInput:

                        # taking first number input from a user
                        firstNum = int(input("Enter the first binary number: "))
                        firstIsBinary = checkBinary(firstNum)
                        if not firstIsBinary:
                            continue

                        # checking whether a number exceeds binary number limit or not
                        firstNumBinaryLimit = binaryCrossover(firstNum)
                        if not firstNumBinaryLimit:
                            continue
                        
                        # taking second number input from a user  
                        secondNum = int(input("Enter the second binary number: "))
                        secondIsBinary = checkBinary(secondNum)
                        if not secondIsBinary:
                            continue
                        
                        # checking whether a number exceeds binary number limit or not
                        secondNumBinaryLimit = binaryCrossover(secondNum)
                        if not secondNumBinaryLimit:
                            continue
                        
                        # showing error message if sum of the numbers exceeds 255
                        if (int(binaryToDec(firstNum))+ int(binaryToDec(secondNum))) > 255:
                            print("")
                            print("\t|--------------------------------------------------------------|")
                            print("\t|                            ERROR!                            |")
                            print("\t|            Sum of the values are greater than 255.           |")
                            print("\t|           Numbers must be less than or equal to 255          |")
                            print("\t|--------------------------------------------------------------|\n")
                            continue
                        else:
                            correctInput = True
                    
                    # adding the numbers to a list named as binList    
                    binList.append(fillBinary(firstNum))
                    binList.append(fillBinary(secondNum))

                    # showing the addition of the numbers
                    print("")
                    print("\t|-------------------------------------------------|")
                    print("\t| 1st binary input        :  ",fillBinary(firstNum),"           |")
                    print("\t| 2nd binary input        :  ",fillBinary(secondNum),"           |")
                    print("\t|                            ----------           |")
                    print("\t| Sum of binary numbers   :  ",addBinary(binList),"           |")
                    print("\t|-------------------------------------------------|\n\n")

                    print("\t[-------After conversion in decimal numbers-------]\n")
                    print("\t|-------------------------------------------------|")
                    print("\t| 1st decimal number       :   ",binaryToDec(firstNum),"              |")
                    print("\t| 2nd decimal number       :   ",binaryToDec(secondNum),"              |")
                    print("\t|                              -----              |")
                    print("\t| Sum of decimal numbers   :   ",fillDecimal(int(binaryToDec(firstNum))+ int(binaryToDec(secondNum))),"              |")
                    print("\t|-------------------------------------------------|\n")
                                    
                    flag = True
                    
                except:
                    # showing an error to the user, if any other vlaue except integer is given
                    print("")
                    print("\t|--------------------------------------------------------------|")
                    print("\t|                        INVALID ATTEMPT!                      |")
                    print("\t|                Please enter only the numbers                 |")
                    print("\t|--------------------------------------------------------------|\n")

        elif(st.lower() == 'd'):
            # decimal number conversion mode
            print("\t<^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^>")           
            print("\t<  Conditions:                                                >")
            print("\t<------------------------------------------------------------->")
            print("\t<  * Sum of the numbers should be less than or equal to 255.  >")
            print("\t<  * Alphabets are not allowed.                               >")
            print("\t<                                                             >")
            print("\t<vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv>\n")
            
            while not flag:
                try:
                    correctInput = False
                    while not correctInput:
                        correctFirstInput = False
                        while not correctFirstInput:
                            try:
                                firstNumInp = input("Enter the first decimal number: ") # taking first number input from a user
                                firstNum=int(firstNumInp) #changes number to int
                                correctFirstInput = True
                            except:
                                try:
                                    # showing an error if a input number is float
                                    val = float(firstNumInp)
                                    print("\t|--------------------------------------------------------------|")
                                    print("\t|                             ERROR!                           |")
                                    print("\t|                  Float value is not accepted.                |")
                                    print("\t|--------------------------------------------------------------|")
                                    continue
                                except:
                                    print("\t|--------------------------------------------------------------|")
                                    print("\t|                             ERROR!                           |")
                                    print("\t|                Please enter the valid numbers only.          |")
                                    print("\t|--------------------------------------------------------------|")
                                    continue

                        # checking whether a number exceeds 255 or not
                        firstNumIsDecimal = decimalCrossover(firstNum)
                        if not firstNumIsDecimal:
                            continue
                            
                        correctSecondInput = False
                        while not correctSecondInput:
                            try:
                                secondNumInp = input("Enter the second decimal number: ") # taking first number input from a user
                                secondNum = int(secondNumInp) #changes number to int
                                correctSecondInput = True
                            except:
                                try:
                                    # showing an error if a input number is float
                                    val = float(secondNumInp)
                                    print("\t|--------------------------------------------------------------|")
                                    print("\t|                             ERROR!                           |")
                                    print("\t|                  Float value is not accepted.                |")
                                    print("\t|--------------------------------------------------------------|")
                                    continue
                                except:
                                    print("\t|--------------------------------------------------------------|")
                                    print("\t|                             ERROR!                           |")
                                    print("\t|                Please enter the valid numbers only.          |")
                                    print("\t|--------------------------------------------------------------|")
                                    continue

                        # checking whether a number exceeds 255 or not
                        secondNumIsDecimal = decimalCrossover(secondNum)
                        if not secondNumIsDecimal:
                            continue
                        
                        if (firstNum+secondNum) > 255:
                            print("\t|--------------------------------------------------------------|")
                            print("\t| Sum of the values are greater than 255.                      |")
                            print("\t| Try Again by entering numbers in a way that is less than 255.|")
                            print("\t|--------------------------------------------------------------|")
                            continue
                        else:
                            correctInput = True   
                    binList.append(decimalToBin(firstNum))
                    binList.append(decimalToBin(secondNum))

                    # showing the addition of the numbers
                    print("")
                    print("\t|-------------------------------------------------|")
                    print("\t| 1st decimal input       :  ",fillDecimal(firstNum),"                |")
                    print("\t| 2nd decimal input       :  ",fillDecimal(secondNum),"                |")
                    print("\t|                            -----                |")
                    print("\t| Sum of decimal numbers  :  ",fillDecimal(firstNum + secondNum),"                |")
                    print("\t|-------------------------------------------------|\n\n")
                    
                    
                    print("\t[--------After conversion in binary numbers--------]\n")
                    print("\t|-------------------------------------------------|")
                    print("\t| 1st binary number       :  ",decimalToBin(firstNum),"           |")
                    print("\t| 2nd binary number       :  ",decimalToBin(secondNum),"           |")
                    print("\t|                            ----------           |")
                    print("\t| Sum of binary numbers   :  ",addBinary(binList),"           |")
                    print("\t|-------------------------------------------------|")

                    flag = True                    
                    
                except:
                    # showing an error to the user, if any other vlaue except integer
                    print("")
                    print("\t|--------------------------------------------------------------|")
                    print("\t|                        INVALID ATTEMPT!                      |")
                    print("\t|                Please enter only the numbers                 |")
                    print("\t|--------------------------------------------------------------|\n")

        elif(st_num == True):
            # checking whether a input from a user in integer number
            print("")
            print("\t|--------------------------------------------------------------|")
            print("\t|                        INVALID ATTEMPT!                      |")
            print("\t|                    Integers are not allowed.                 |")
            print("\t|        Please enter the correct values and try again         |")
            print("\t|--------------------------------------------------------------|\n")
        elif (st == ""):
            # checking whether a input from a user empty
            print("")
            print("\t|--------------------------------------------------------------|")
            print("\t|                        INVALID ATTEMPT!                      |")
            print("\t|                     Empty Field not allowed.                 |")
            print("\t|--------------------------------------------------------------|\n")
           
        else:
            # checking whether a input from a user is invalid
            print("")
            print("\t|--------------------------------------------------------------|")
            print("\t|                        INVALID ATTEMPT!                      |")
            print("\t|        Please enter the correct values and try again.        |")
            print("\t|--------------------------------------------------------------|\n")
            flag = False
