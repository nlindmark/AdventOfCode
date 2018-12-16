import re
from collections import defaultdict


def parse(input,sum):

    if not input:
        return(sum)
    elif(input[0] == 0):
        #No subnodes
        input.pop(0)
        for i in range(input.pop(0)):
            sum += input.pop(0)
        return(sum)
    else:
        
        nodes = input.pop(0)
        refs = input.pop(0)

        
        tmp = defaultdict(int)
        for node in range(nodes):

            tmp[node+1] = parse(input, sum)
        
        for i in range(refs):
            refnode = input.pop(0)
            sum += tmp[refnode]
        
        return(sum)




def solve(filename):

    
    
    file = open(filename, "r")
    input = file.readlines()
    input = input[0].split(" ")
    input = [int(i) for i in input]
    file.close()
        
    sum = 0
    sum = parse(input, sum)

    
    print(sum)


    

    

   


    return(sum)

print("Solution is {}".format(solve("testdata1.txt")))
