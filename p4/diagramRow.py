class DiagramRow():
	
	def __init__(self, pitch, length, fillChar='-'):
		self.pitch = pitch
		self.length = length
		self.fillChar = fillChar
		self.listRep = []
		for i in range(length):
			self.listRep.append(fillChar)

	def addNote(self, pos, l=1):
		for i in range(l):
			self.listRep[pos+i] = '*'

	def getString(self):
		tempStr = str(self.pitch) + ': '
		for c in self.listRep:
			tempStr += str(c)
		return tempStr
