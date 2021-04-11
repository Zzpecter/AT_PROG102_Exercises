from parkVisit import ParkVisit
class Person():
    
    def __init__(self, name):
        self.name = name
        self.visits = []

    def addVisit(self, arrival, departure):
        visit = ParkVisit(arrival, departure)
        self.visits.append(visit)

    def show(self):
        lines = []
        lines.append(self.name)
        for v in self.visits:
            lines.append(str(v.arrival) + ' ' + str(v.departure) + ' ' +  str(v.totalTime))
        return print(lines)

    def calculateFare(self, fare):
        timeSum = 0
        for v in self.visits:
            timeSum += v.totalTime
        return fare*timeSum
