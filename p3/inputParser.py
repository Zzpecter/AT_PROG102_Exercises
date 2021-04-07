from bin import asciiDigit
import time

class InputParser():
	def sumStringToAscii(inputStr):
		#locate and read the values of 'a', 'b' and '+'
		if controlString(inputStr):

			i = 0
			charBuffer = ''
			a=0
			b=0
			for digit in inputStr:
				if digit == '+':
					
					try:
					    a = int(charBuffer)
					except ValueError:
					    print('{} Must be the sum of two integer numbers!'.format(inputStr))

					charBuffer = ''
				else:
					charbuffer += digit
			try:
			    b=int(charBuffer)
			except ValueError:
			    print('{} Must be the sum of two integer numbers!'.format(inputStr))
		else:
			print('{} Must be the sum of two integer numbers!'.format(inputStr))

	def controlString(inputStr):
		isNum = True
		containsPlusSign = False

		for digit in inputStr:
			if not digit.isNumeric():
				if digit == '+':
					containsPlusSign = True
				else:
					isNum = False

		return (isNum and containsPlusSign)

	def getDigits(inputAscii, numDigits):
		#number of chars to complete a line, based on numdigits
		#space of each digit + 1 space for each but the last
		spaceIndexes = (5, 11, 17, 23, 29, 35, 41, 47, 53, 60)
		Digits = []
		count = 0
		currentDigit = 0

		for i in range(numDigits):
			Digits.append([])

		for char in inputAscii:

			
			if char == '\n':
				currentDigit = 0
				count = 0

			elif count in spaceIndexes:
				currentDigit += 1
				count += 1
			else:
				Digits[currentDigit].append(char)
				count += 1

			
		return Digits

	def solveSum(stringedSum):
		a = 0
		b = 0
		subString = ''
		for c in stringedSum:
			if c == '+':
				a = int(subString)
				subString = ''
			else:
				subString += c

		b = int(subString)
		return a+b

	def getString(digits, save=False, filename=None):
		resultString =''
		NUM_LINES = 7
		ROWS_PER_DIGIT = 5
		spaceIndexes = (5, 11, 17, 23, 29, 35, 41, 47, 53, 60)
		firstIte =True

		#number of chars in a row, adding spaces
		charsInRow = (ROWS_PER_DIGIT * len(digits)) + (len(digits) - 1) 
		actualDigitCharCount = 0
		actualDigitIdx = 0

		for line in range(NUM_LINES):
			actualDigitIdx = 0
			actualDigitCharCount = line * ROWS_PER_DIGIT
			if not firstIte:
				resultString +='\n'
			else:
				firstIte = False 
			for i in range(charsInRow):
				
				#new line
				if i in spaceIndexes:
					actualDigitIdx += 1
					actualDigitCharCount = line * ROWS_PER_DIGIT
					resultString +='.' #add the space
				else:
					resultString += digits[actualDigitIdx][actualDigitCharCount]
					actualDigitCharCount += 1

		if save:
			if filename == None:
				filename = round(time.time() * 1000)
			txt = open("input/{}.txt".format(filename), "w+")
			txt.write(resultString)
			txt.close()
		return resultString

