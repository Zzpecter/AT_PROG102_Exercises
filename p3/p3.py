from inputParser import InputParser as ip
from bin.asciiDigit import AsciiDigit as ad

import argparse


def getDigitsNumber(rawInput):
        charCount=0
        digitCount=0
        line=0
        auxDigit=[]
        space = False
        for char in rawInput:
            charCount += 1
            if space:
                pass
                space=False
            if charCount == 6:
                digitCount += 1
                space = True
                charCount = 0
            if char == '\n':
                #next line
                break


        return(digitCount)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='p3.py')
    parser.add_argument('--inputFile', type=str, default='input/121plus9.txt',  help='select a txt file with the input')
    opt = parser.parse_args()
    print(opt.inputFile)

    with open(opt.inputFile, 'r') as file:
        dataRaw = file.read().replace(' ', '')
    #send input data to the next functions
    numDigits = getDigitsNumber(dataRaw)
    digits = ip.getDigits(dataRaw, numDigits)

    aDig = ad()
    stringInput = ''
    for d in digits:
        stringInput += aDig.digitToChar(d)
    print(stringInput)
    result = ip.solveSum(stringInput)
    print(str(result))



    resultDigits=[]
    for c in str(result):
        resultDigits.append(aDig.charToDigit(c))
    print(len(resultDigits))

    output = ip.getString(resultDigits)
    print(output)

