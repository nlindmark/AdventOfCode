from collections import defaultdict

def solve(filename):
    file = open(filename, "r") 

    sum = 0 
    f = defaultdict(int)

    while(1):
        for line in file:
            freq = int(line)
            sum += freq
            print(freq,sum)
            if(f[sum] == 1):
                file.close()
                return(sum)
            else:
                f[sum] = 1
        file.seek(0)
  
    

print("Solution is " + str(solve("puzzledata.txt")))

