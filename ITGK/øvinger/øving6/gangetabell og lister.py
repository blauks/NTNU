def seperate(number, threshold):
    list1 = []
    list2 = []
    for x in range(len(number)):
        if number[x] < threshold:
            list1.append(number[x])
        else:
            list2.append(number[x])
    
    return list1, list2


liste = [1,2,3,4,5,6]
print(seperate(liste,3))

def multiplication_table(n):
    liste = []
    listeLiten = []
    for x in range(1,n+1):
        for y in range(1,n+1):
            listeLiten.append(x*y)
        liste.append(listeLiten) 
        listeLiten = []
    return liste

print(multiplication_table(4))

