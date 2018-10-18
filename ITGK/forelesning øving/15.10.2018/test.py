def Fac(n):
    if n == 0:
        return 1
    else:
        sumN = 1
        for x in range(1,n+1):
            sumN *= x #eller sumN = sumN*x
        return sumN

print(Fac(6))

def nChoosek(n,k):
    sumN = Fac(n)
    sumK = Fac(k)
    sumNoK = Fac(n-k)
    return sumN/(sumK * sumNoK)
    

def Pascal(n):
    for x in range(n):
        for y in range(x+1):
            print(nChoosek(x,y), end=' ')
        print()
    
Pascal(4)    
        

