from input import *

print("")
print("\t<ʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌ>")
print("\t<                                                              >")
print("\t<                             WELCOME!                         >")
print("\t<                        PYTHON BYTE ADDER.                    >")
print("\t<                                                              >")
print("\t<                                                ~Sachin Dahal >")
print("\t<vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv>\n")

inputNo() # calling the input function to be executed

# Setting up a condition for a continuing section 
isCont = False
while not isCont:
    contInput = input("\nDo you want to continue? [Y/N] ")
    if(contInput.lower() == 'y'):
        inputNo()
    elif (contInput == ""):
        print("")
        print("\t|--------------------------------------------------------------|")
        print("\t|                              ERROR!                          |")
        print("\t|                     Empty field not allowed.                 |")
        print("\t|--------------------------------------------------------------|\n")
        isCont = False
    else:
        print("")
        print("\t<ʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌʌ>")
        print("\t<                                                              >")
        print("\t<            THANK YOU FOR USING THIS ADDER TOOL!              >")
        print("\t<                        HAVE A NICE DAY.                      >")
        print("\t<                                                              >")
        print("\t<                                                ~Sachin Dahal >")
        print("\t<vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv>\n")
        isCont = True

# end of the program

