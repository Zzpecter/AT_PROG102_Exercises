#BUG: bufferStr @ Line 22 adds different structure than inputLines, needs to be the same.


import argparse
from person import Person
from dailyReport import DailyReport

FARE = 0.1
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='p7.py')
    parser.add_argument('--inputFile', type=str, default='input/sample1.txt',  help='select a txt file with the input')
    opt = parser.parse_args()

    with open(opt.inputFile) as f:
        inputLines = f.readlines()

    entryLogsPerDay = [] # string list of logs separated by days
    bufferStr = []
    for l in inputLines:
        if l == 'OPEN\n':
            bufferStr = []
        elif l == 'CLOSE' or l == 'CLOSE\n':
            entryLogsPerDay.append(bufferStr)
        else:
            bufferStr.append(l)

    dayCount = 0
    visitorsPerDay = {}
    for day in entryLogsPerDay:
        names = []
        visitors = []
        for l in day:
            action, name, time = l.split(' ')

            if name in names:
                pass
            else:
                names.append(name)

        #iterate over names to create persons and their respective visits
        for n in names:
            arrivals = []
            departures = []
            for l in day:
                action, name, time = l.split(' ')

                if n == name:
                    if action == 'ENTER':
                        arrivals.append(time)
                    elif action == 'EXIT':
                        departures.append(time)


            tempPerson = Person(n)
            for a, d in zip(arrivals, departures):
                tempPerson.addVisit(a, d)
            visitors.append(tempPerson)

        visitors.sort(key=lambda x: x.name, reverse=False)
        visitorsPerDay.update({dayCount: visitors})
        dayCount += 1

    for key, value in visitorsPerDay.items():
        print(f'Day: {key + 1}')
        #value is a list of persons
        for p in value:
            val = p.calculateFare(FARE)
            outStr = f'{p.name}: ${val:.2f}'
            print(outStr)


