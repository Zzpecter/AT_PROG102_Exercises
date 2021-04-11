class ParkVisit():
    
    def __init__(self, arrival, departure):
    	self.arrival = int(arrival)
    	self.departure = int(departure)
    	self.totalTime = self.departure - self.arrival
