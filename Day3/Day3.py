import re


def parse(str):
    str = str.replace("#","").replace("@",":").replace("x",",").replace(" ","").strip()

    lst = str.split(":")
    lst2 = [lst[0]]
    lst2.append(lst[1].split(","))
    lst2.append(lst[2].split(","))
    lst2[1] = convertToPoints(lst2[1], ['2','2'])
    lst2[2] = convertToPoints(lst2[1], lst2[2])

    return(lst2)

def convertToPoints(lst1, lst2):
    lst2[0] = int(lst1[0]) + int(lst2[0]) - 1
    lst2[1] = int(lst1[1]) + int(lst2[1]) - 1

    return lst2

def doOverlap(r1, r2):

    if(r1[2][0] < r2[1][0]):
        #r1 is to the left of r2
        return(False)

    if(r1[2][1] < r2[1][1]):
        #r1 is above of r2
        return(False)
    
    if(r2[2][0] < r1[1][0]):
        #r2 is to the left of r1
        return(False)

    if(r2[2][1] < r1[1][1]):
        #r2 is above of r1
        return(False)
    
    return(True)
    

def intersection(r1, r2):
        
        
    ax1 = r1[1][0]
    ax2 = r1[2][0]
    bx1 = r2[1][0]
    bx2 = r2[2][0]
    ay1 = r1[1][1]
    ay2 = r1[2][1]
    by1 = r2[1][1]
    by2 = r2[2][1]

    x1 = max(min(ax1, ax2), min(bx1, bx2))
    y1 = max(min(ay1, ay2), min(by1, by2))
    x2 = min(max(ax1, ax2), max(bx1, bx2))
    y2 = min(max(ay1, ay2), max(by1, by2))
    
    return [[x1, y1],[x2, y2]]
    

def rect2points(r1, dic):
    for x, y in [(x,y) for x in range(r1[0][0],r1[1][0]+1)  for y in range(r1[0][1],r1[1][1]+1)]:
        #print(x,y)
        dic[(x,y)] = 1

def overlapSize(r1, r2):
    size = abs((r1[1][0] - r2[1][0]) * (r1[2][1] - r2[2][1]))

    return(size)



def solve(filename):
    file = open(filename, "r") 
    
    line = file.readlines()

    dic = {}

    sum = 0
    for x, y in [(x,y) for x in line for y in line]:
        x = parse(x)
        y = parse(y)

        if(x != y and doOverlap(x,y)):
            sum += overlapSize(x,y)
            ri = intersection(x,y)
            rect2points(ri, dic)
  
    

    file.close()
    return(len(dic)) 
    

print("Solution is " + str(solve("puzzledata.txt")))

