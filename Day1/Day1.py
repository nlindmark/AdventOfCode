
def solve(filename):
    file = open(filename, "r") 

    sum = 0 
    for line in file:
        sum += float(line)

  
    file.close()
    return(sum)
    

print("Solution is " + str(solve("puzzledata.txt")))

