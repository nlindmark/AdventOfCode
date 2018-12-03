import string

def isClose(str1, str2):
    l1 = list(str1.strip())
    l2 = list(str2.strip())

    misses = 0
    i = 0
    while(i < len(l1)):
        if(l1[i] != l2[i]):
            misses += 1
        i+=1
    

    return(misses <= 1)

def commonChars(str1, str2):
    l1 = list(str1.strip())
    l2 = list(str2.strip())

    res = []
    i = 0
    while(i < len(l1)):
        if(l1[i] == l2[i]):
            res.append(l1[i])
        i+=1
    return("".join(res))


def solve(filename):
    
    file = open(filename, "r") 

    line = file.readlines()
    i=0
    j=0
    
    while(i<len(line)-1):
        j = i+1
        while(j<len(line)):
            if(isClose(line[i], line[j])):
                return(commonChars(line[i], line[j]))                   
            j+=1
        i+=1
        

  
    file.close()
    return("")
    

print("Solution is " + str(solve("puzzledata.txt")))

