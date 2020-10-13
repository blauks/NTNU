flag3Mod = 2003824372959068486
nextPrime = 18446744073709551629

x = 0

s = 0

while s != flag3Mod:
    s = 2^x%nextPrime
    x+=1
    print(x)
