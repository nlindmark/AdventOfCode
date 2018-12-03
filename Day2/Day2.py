import string

def solve(filename):
    file = open(filename, "r") 

    chars = list(string.ascii_lowercase)
    dir = {"two":0, "three":0}

    for line in file:
        for x in chars:
            if(line.count(x) == 2):
                dir["two"] += 1
                break
        for x in chars:
            if(line.count(x) == 3):
                dir["three"] += 1
                break

    
  
    file.close()
    return(dir["two"] * dir["three"])
    

print("Solution is " + str(solve("puzzledata.txt")))

