liste = [2,4,6,8,10,12,14,16,18,20]
i = 1

for x in range(0,len(liste),2):
    liste[x] = i * 3
    i = i + 1

print(liste)

