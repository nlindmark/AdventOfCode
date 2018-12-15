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
        metachs = input.pop(0)
        for node in range(nodes):
            sum = parse(input, sum)
        
        for i in range(metachs):
            sum += input.pop(0)
        
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
