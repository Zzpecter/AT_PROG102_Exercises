from path import Path
class TrafficLight(Path):
	
	def __init__(self, redDuration, greenDuration):
		self.redDuration = redDuration
		self.greenDuration = greenDuration
		self.currentLight = 'RED' #RED or GREEN
		self.nextChange = redDuration # starts at the beginning of red
		self.speed = 0 #you have to stop at red

	def tick(self):
		if self.nextChange > 1:
			self.nextChange -= 1
		else:
			if self.currentLight == 'RED':
				self.currentLight = 'GREEN'
				self.nextChange = self.greenDuration
			else:
				self.currentLight = 'RED'
				self.nextChange = self.redDuration

	def getSpeed(self):
		return 1 if self.currentLight == 'GREEN' else 0