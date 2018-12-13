import re
from collections import defaultdict



class Point:
    def __init__(self,x,y,name = None):
        self.x = x
        self.y = y
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
    
    def samexory(self, other):
        if(self.x == other.x or self.y == other.y):
            return(True)
        else:
            return(False)
    
    def totalDistance(self, plist):
        sum=0
        for p in plist:
            sum += self.distance(p)
        return(sum)
    

def findGrid(plist):
    pmax = Point(0,0)
    pmin = Point(999,999)
    for p in plist:
        if(p.x < pmin.x):
            pmin.x = p.x
        if(p.y < pmin.y):
            pmin.y = p.y
        if(p.x > pmax.x):
            pmax.x = p.x
        if(p.y > pmax.y):
            pmax.y = p.y

    return((pmin, pmax))

def findClosest(ptarget, plist):
    
    
    pclosest = Point(999,999)
    for p in plist:
        if(p.distance(ptarget) < pclosest.distance(ptarget)):
            pclosest = p
    
    #But is it unique
    pother = Point(999,999)
    for p in reversed(plist):
        if(p.distance(ptarget) < pother.distance(ptarget)):
            pother = p

    if(not(pclosest is pother)):
        peq = Point(pclosest.x, pclosest.y, ".")
        return(peq, peq.distance(ptarget))
    else:
        return( (pclosest,pclosest.distance(ptarget)) )
    
def generateProximityMap(pntlist):

    (pmin, pmax) = findGrid(pntlist)
    
    tmp = ""
    resmap = defaultdict(list)
    for i in range(pmin.y,pmax.y+1):
        for j in range(pmin.x,pmax.x+1):
            target = Point(j,i)
            (pc, pcd) = findClosest(target, pntlist)
            tmp += pc.name
            #print(target, pc, pcd)
            if(pc.name == "."):
                continue             
            resmap[pc.name].append(target)
        #print(tmp)
        tmp = ""
    return(resmap)

def ontheBoarder(pt, plist):
    for p in plist:
        if(p.samexory(pt)):
            return(True)
    return(False)

def findMaxFiniteArea(pmin, pmax, resmap):

    max = 0

    for (name, plist) in resmap.items():
        if( ontheBoarder(pmin, plist) or ontheBoarder(pmax, plist) ):
            continue
        elif (len(plist) > max):
            max = len(plist)

    return(max)

def calcProxyRegion(pmin,pmax,mindistance,plist):

    area = 0    
    for i in range(pmin.y,pmax.y+1):
        for j in range(pmin.x,pmax.x+1):
            target = Point(j,i)
            dist = target.totalDistance(plist) 
            if(dist < mindistance):
                area += 1

    return area

def solve(filename, mindistance):

    pntlist = []

    file = open(filename, "r")
    pntName = 0
    for line in file:
        x,y = line.split(",")
        pntlist.append(Point(int(x), int(y),str(pntName)))
        pntName += 1

    file.close()
    
    (pmin, pmax) = findGrid(pntlist)
    maxarea = calcProxyRegion(pmin, pmax, mindistance, pntlist)


    return(maxarea)

print("Solution is {}".format(solve("puzzledata.txt", 10000)))
