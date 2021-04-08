
class Peg():
	
	def __init__(self, color, pos):
		self._color = color
		self._pos = pos
		self._matched = False

	def getColor(self):
		return self._color
	def setColor(self, color):
		self._color = color
	def getPos(self):
		return self._pos
	def setPos(self, pos):
		self._pos = pos
	def getMatched(self):
		return self._matched
	def setMatched(self, matched):
		self._matched = matched