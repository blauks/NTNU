def multi(t):
    count = 1
    prod = 1
    diff = 1
    x = 1
    while diff>t:
        prod2 = prod 
        prod = prod*(1+(1/x**2))
        diff = prod - prod2
        count = x
        x += 1
    return prod, count

tol = float(input("Velg en toleransegrense: "))
print("Produktet ble",multi(tol)[0],"etter",multi(tol)[1],"iterasjoner")