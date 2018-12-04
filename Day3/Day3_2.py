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
    


    



def diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 


def solve(filename):
    file = open(filename, "r") 
    
    line = file.readlines()

    ilist = {}
    olist = {}

    sum = 0
    for x, y in [(x,y) for x in line for y in line]:
        x = parse(x)
        y = parse(y)

        ilist[x[0]] = 1
        
        if(x != y and doOverlap(x,y)):
            olist[x[0]] = 1
    

    file.close()

    res = diff(list(ilist.keys()), list(olist.keys()))
    return(res[0]) 
    

print("Solution is " + str(solve("puzzledata.txt")))

