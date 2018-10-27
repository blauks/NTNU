aStreng = input("Skriv inn en streng: ")
def hverFjerde(s):
    for x in range(0,len(s),4):
        print(aStreng[x], end="")
    print()

hverFjerde(aStreng)

bListe = ["sabel","kan","mestr","kuleis"]
def sisteBokstaver(l):
    for x in bListe:
        print(x[-2:],end="")
    print()

sisteBokstaver(bListe)

#Kodesnutt 1 Korrekt
streng = "I Want Cake"
#streng[7:] = "Cupcake" Kan ikke endre det som står i stringen
print(streng)
 
#Kodesnutt 2 Korrekt
streng = "I Want Cake"
streng = streng[-4:100:]
print(streng)
 
#Kodesnutt 3
streng = "I Want Cake"
#streng = streng[] Streng er ikke en liste
print(streng)