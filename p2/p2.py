from trafficLight import TrafficLight
from road import Road


if __name__ == '__main__':

    #input handling
    invalidInput = True
    while invalidInput:

        print('Enter the Number of traffic lights:')
        n = input()
        try:
            n=int(n)
        except ValueError:
            print('Must enter integer numbers!')
            pass
        print('Enter the length of the road:')
        l = input()
        try:
            l=int(l)
        except ValueError:
            print('Must enter integer numbers!')
            pass

        trafficLights = []
        distances = []
        for light in range(n):
            print(f'Enter the distance at which traffic light #{light} is located:')
            d = input()
            try:
                d=int(d)
            except ValueError:
                print('Must enter integer numbers!')
                pass
            print(f'Enter the red light duration for traffic light #{light}:')
            r = input()
            try:
                r=int(r)
            except ValueError:
                print('Must enter integer numbers!')
                pass
            print(f'Enter the green light duration for traffic light #{light}:')
            g = input()
            try:
                g=int(g)
            except ValueError:
                print('Must enter integer numbers!')
                pass
            trafficLights.append(TrafficLight(r, g))
            distances.append(d)
        invalidInput = False

    #building the roadmap
    roadmap = []
    for tile in range(l):

        #traffic light check:
        if tile in distances:
            idx = distances.index(tile)
            roadmap.append(trafficLights[idx])
        #road
        else:
            roadmap.append(Road(1))

    #simulating the trip
    truckPos = 0
    travelTime = 0

    while truckPos < l:

        truckSpeed = roadmap[truckPos].getSpeed()
        truckPos += truckSpeed
        print(f'truck Pos: {truckPos} speed: {truckSpeed} time: {travelTime}')
        for tl in trafficLights:
            tl.tick()
            print(f'now: {tl.currentLight} next in: {tl.nextChange}')
        travelTime += 1

    print(travelTime)
