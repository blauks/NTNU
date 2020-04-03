fil = open("primes.txt", "a")

def fermat(a):
    return (2)**(a-1)%a == 1

x = 2

fil.write("1" + "\n")
fil.write("2" + "\n")

while True:  
    if fermat(x):
        fil.write(str(x) + "\n")
        print(x)
    
    x += 1
