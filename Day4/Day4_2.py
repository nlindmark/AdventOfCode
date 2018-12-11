from collections import defaultdict

def parseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])


def solve(filename):

    file = open(filename, "r")
    lines = file.read().split('\n')
    lines.sort()
    

    G = defaultdict(int) # [Guard: Total sleep time] 
    GM = defaultdict(int) # [(Guard, minute): Sleep this minute]
    guard = None
    asleep = None

    for line in lines:
        if line:
            time = parseTime(line)
            if 'begins shift' in line:
                guard = int(line.split()[3][1:])
                asleep = None
            elif 'falls asleep' in line:
                asleep = time
            elif 'wakes up' in line:
                for t in range(asleep, time):
                    GM[(guard, t)] += 1
                    G[guard] += 1
    
    file.close()

    def argmax(d):
        best = None
        for k,v in d.items():
            if best is None or v > d[best]:
                best = k
        return best

    def argmax2(d,g):
        best = None
        for k,v in d.items():
            if (k[0]==g) and (best is None or v > d[best]):
                best = k
        return best


    (guard, minute) = argmax(GM)

    

    return(guard * minute)

print("Solution is {}".format(solve("puzzledata.txt")))
