from gates import *

# function to carry addition of binary numbers
def addBinary(binList):
    binList1 = binList[0]
    binList2 = binList[1]
    carryIn = 0
    finalValue = ""
    for i in range(len(binList1)-1,-1,-1):
        upperBit = int(binList1[i])
        lowerBit = int(binList2[i])
        x_or = xorGate(upperBit,lowerBit) #xorGate
        sum = xorGate(x_or,carryIn) #xorGate
        and_gate1 = andGate(upperBit,lowerBit)
        and_gate2 = andGate(x_or,carryIn)
        carryOut = orGate(and_gate1,and_gate2)
        carryIn = carryOut
        finalValue = str(sum) + finalValue
    return finalValue

