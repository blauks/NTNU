import math

def divisable(x,y):
    if x%y==0:
        return True
    else:
        return False

def isPrime(a):
    prime = False
    for tall in range(2,a):
        if divisable(a,tall):
            prime = False
            break
        else:
            prime = True
    return prime

def isPrime2(a):
    prime = False
    i = 3
    if a%2 != 0 and a != 2:
        while i < round(math.sqrt(a) + 0.5):
            if divisable(a,i):
                prime = False
                break
            else:
                prime = True
            i = i + 2
    else:
        prime = True
    return prime    

t1 = int(input("Hvilket tall vil du sjekke om er et primtall: "))

print(isPrime2(t1))