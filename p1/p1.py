from peg import Peg
from pegCollection import PegCollection


if __name__ == '__main__':
	#input handling
	invalidInput = True
	while invalidInput:

		print('Enter the length of the Code!')
		l = input()
		print('Enter the Code!')
		code = input().upper()
		print('Now enter the Guess:')
		guess = input().upper()

		#input validation
		try:
		    l=int(l)
		except ValueError:
		    print('{} Must be integer numbers!'.format(l))

		if len(code) == len(guess) == l:
			invalidInput = False

		print(l, code, guess)


	#create the peg and pegCollection objects
	pegs = []
	i=0
	for c in code:
		p = Peg(color=c, pos=i)
		i += 1
		pegs.append(p)
	codePegs = PegCollection(pegs)

	pegs = []
	i=0
	for c in guess:
		p = Peg(color=c, pos=i)
		i += 1
		pegs.append(p)
	guessPegs = PegCollection(pegs)

	#calculate r and s
	r = codePegs.getR(guessPegs)
	s = codePegs.getS(guessPegs, r)

	print(f'{r}, {s}')



