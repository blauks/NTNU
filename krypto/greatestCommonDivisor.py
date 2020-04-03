import sys
import math

#a = int(sys.argv[1])
#b = int(sys.argv[2])

streng = ""

for x in range(1,40):
    r = [x,40]

    k = 1

    while not r[k] == 0:
        q =  math.floor(r[k-1]/r[k])
        r.append(r[k-1] - q*r[k])
        k = k + 1
    
    if(r[k-1] == 1):
        streng += str(x) + ", "

print(streng)