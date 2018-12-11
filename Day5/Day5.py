import re



def solve(filename):

    file = open(filename, "r")
    poly = file.read()
    file.close()
    

    #print(poly)


    polyLen = len(poly)
    iterations = 0
    while(True):
        newPoly = re.sub(r'aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz',"",poly)
        iterations += 1
        if(len(newPoly) == polyLen):
            break
        
        poly = newPoly
        polyLen = len(newPoly)


    

    return(len(poly))

print("Solution is {}".format(solve("puzzledata.txt")))
