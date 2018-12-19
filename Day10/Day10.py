import re
import copy
from collections import defaultdict


class Point:
    def __init__(self,x,y,vx,vy,name = None):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        if(name is None):
            self.name = ""
        else:
            self.name = name

    def distance(self, p):
        return ( abs(self.x - p.x) + abs(self.y - p.y) )

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False

    def __lt__(self, other):
        if (self.x < other.x) and (self.y < other.y):
            return True
        elif (self.x < other.x) and (self.y > other.y):
            return True
        else:
            return False
    def distance(self, other):
        return ( abs(self.x - other.x) + abs(self.y - other.y) )


    
    def tick(self):
        self.x += self.vx
        self.y += self.vy

        return (self)

def findCenterOfGravity(plist):

    pcenter = Point(0,0,0,0)
    for p in plist:
        pcenter.x += p.x
        pcenter.y += p.y
    pcenter.x /= len(plist)
    pcenter.y /= len(plist)

    return pcenter

def calcDistance(plist):
    pcenter = findCenterOfGravity(plist)

    sum = 0
    for p in plist:
        sum += p.distance(pcenter)
    
    return (sum)


def findGrid(plist):
    pmin = Point(1000000,10000000,0,0)
    pmax = Point(-1000000,-1000000,0,0)
    for p in plist:
        if(p.x < pmin.x):
            pmin.x = p.x - 1
        if(p.y < pmin.y):
            pmin.y = p.y -1
        if(p.x > pmax.x):
            pmax.x = p.x + 1
        if(p.y > pmax.y):
            pmax.y = p.y + 1

    return((pmin, pmax))

def printGrid(pmin, pmax, plist):

    for y in range(pmin.y, pmax.y + 1 ):
        line = ""
        for x in range(pmin.x, pmax.x + 1):
            tmp = Point(x,y,0,0)
            found = False
            for p in plist:
                if(p == tmp):
                    line += "#"
                    found = True
                    break
            if(not found):
                line += "."
        print(line)





def solve(filename):

    
    plist = []

    file = open(filename, "r")

    for line in file:
        tmp = line.replace("position=<","").replace("velocity=<","").replace(">","").replace(", "," ").replace("  ", " ").strip()
        tmp = tmp.split(" ")

        plist.append(Point(int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3])))

    
    file.close()

    
    # Search for min distance
    ptmp = []
    for p in plist:
        ptmp.append(copy.deepcopy(p))

    dmin = calcDistance(ptmp)
    dindex = 0 
    for i in range(12000): 
        new_list = [p.tick() for p in ptmp]
        if(dmin > calcDistance(new_list)):
            dmin = calcDistance(new_list)
            dindex = i
            #print ("index {}: Sum {}".format(dindex,dmin))


    # Spool to min distance
    for i in range(dindex): 
        new_list = [p.tick() for p in plist]

    # make some prints
    new_list = [p.tick() for p in plist]
    (pmin, pmax) = findGrid(new_list)
    printGrid(pmin, pmax, new_list)
    
    

    return(dindex+1)

print("Solution is {}".format(solve("puzzledata.txt")))
