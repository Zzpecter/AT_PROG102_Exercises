class Note():
	
	def __init__(self, pitch, duration, pos):
		self.pitch = pitch
		self.duration = duration if duration is not None else 1
		self.pos = pos