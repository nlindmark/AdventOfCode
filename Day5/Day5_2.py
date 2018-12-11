import re



def solve(filename):

    file = open(filename, "r")
    poly = file.read()
    file.close()

    def reduce(poly):
        polyLen = len(poly)
        iterations = 0
        while(True):
            newPoly = re.sub(r'aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz',"",poly)
            iterations += 1
            if(len(newPoly) == polyLen):
                return(polyLen)
            
            poly = newPoly
            polyLen = len(newPoly)


    unitList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    minLength = len(poly)
    for unit in unitList:
        improvedPoly = re.sub(unit,"",poly, flags=re.IGNORECASE) 
        improvedPolyLen = reduce(improvedPoly)
        if(improvedPolyLen < minLength):
            minLength = improvedPolyLen
            bestunit = unit  


    print("Best unit is {} with len {}".format(bestunit, minLength)) 

    return(minLength)

print("Solution is {}".format(solve("testdata1.txt")))
