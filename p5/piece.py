class Piece():
	
	def __init__(self, kind, color, col, row):
		self.colCodes = ('a', 'b','c', 'd','e', 'f','g', 'h')
		self.kind = kind #{'K', 'Q', 'R', 'B', 'N', ''}
		self.color = color
		self.col = self.colCodes[col]
		self.row = row + 1