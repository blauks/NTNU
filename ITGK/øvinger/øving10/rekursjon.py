def recursiveSum(n):
    if n > 0:
        return n + recursiveSum(n-1)
    else:
        return n

print(recursiveSum(53))

def fakultet(n):
    if n > 1: 
        return n * fakultet(n-1)
    else:
        return n

print(fakultet(5))

def findSmallestElement(numbers):
    try:
        if numbers[0] < numbers[1]:
            del numbers[1]
        else:
            del numbers[0]
        findSmallestElement(numbers)
    except IndexError:
        print(numbers[0])

liste = [5,3,7,1,4,6,9]

findSmallestElement(liste)

