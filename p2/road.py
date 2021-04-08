from path import Path
class Road(Path):
	
	def __init__(self, speed):
		self.speed = speed
	def getSpeed(self):
		return self.speed 