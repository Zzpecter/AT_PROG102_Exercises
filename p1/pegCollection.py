class PegCollection():
	
	def __init__(self, pegs):
		self._pegs = pegs
	def getPegs(self):
		return self._pegs
	def setPegs(self, pegs):
		self._pegs = pegs
	def getPeg(self, pos):
		return self._pegs[pos]


	def getString(self):
		string=''
		for peg in self.getPegs():
			string += peg.getColor()
		return string
	"""
	Assumes self is the code and other is the guess
	"""
	def getR(self, other):
		#same pos and color
		r = 0
		for pos in range(len(self._pegs)):
			if self.getPeg(pos).getColor() == other.getPeg(pos).getColor():
				r += 1

		return r

	def getS(self, other, r):
		#same pos and color
		s = 0
		codeChars = set(self.getString())
		guessChars = set(other.getString())
		
		#intersection
		sChars = codeChars & guessChars

		s = len(sChars)
		s -= r
		return s
