from bin.asciiDigit import AsciiDigit as ad
from inputParser import InputParser as ip

print('Please enter a sum of two positive numbers: (eg. 254+65)')
inputString = input()
resultDigits = []
aDig = ad()

for c in inputString:
   	resultDigits.append(aDig.charToDigit(c))

print(resultDigits[0])
print(resultDigits[1])
print(resultDigits[2])
output = ip.getString(resultDigits, save =True, filename=inputString)
print('Output: {} saved as ASCII Art!'.format(inputString))
