import re
from collections import defaultdict








def remove(c, steps):
    for s, dep in steps.items(): 
        steps[s] = dep.replace(c,"")

    return(steps)

def part1(steps, chrlst):
    #First steps
    order = ""
    while(len(chrlst) > 0):
        for c in chrlst:
            if (not c in steps or len(steps[c]) == 0):
                # I can execute step c
                order += c
                steps = remove(c, steps)
                chrlst.remove(c)

                break
    return(order)


def part2(steps, chrlst, workers):
    
    time = 0

    #Init workers
    w = {}
    for i in range(0,workers):
        w[i] = 0


    order = ""
    inprog = defaultdict(str)

    while(len(chrlst) > 0):
        for c in chrlst:
            if (not c in steps or len(steps[c]) == 0) and not c in inprog:
                # I can execute step c if I have workers free
                for i,t in w.items():
                    if(t <= time):
                        endtime = time +1 + ord(c) - ord('A') + 60 
                        w[i] = endtime 
                        inprog[c]= endtime
                        order += c

                        
                        break
                    else:
                        continue
                

        time += 1

        for c,t in inprog.items():
            if(time == t):
                steps = remove(c, steps)
                chrlst.remove(c)
                print(c,time)
                
        

    return(time)


def solve(filename, workers):

    steps = defaultdict(str)
    chrlst = []
    file = open(filename, "r")
    for line in file:
        tmp = (line.split(" "))
        steps[tmp[7]] += tmp[1]
        chrlst.append(tmp[1])
        chrlst.append(tmp[7])

    file.close()
    
    #Make unique and sort
    tmpset = set(chrlst)
    chrlst = sorted(list(tmpset))

    order = part2(steps, chrlst,workers)

    

    print(order)


    

    

   


    return(order)

print("Solution is {}".format(solve("puzzledata.txt",5)))
