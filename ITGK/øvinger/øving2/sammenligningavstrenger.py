#a
a = input("Skriv in første matvare: ")
b = input("Skriv inn andre matvare: ")
if a.upper() == b.upper():
    print("Samme vare")
else:
    print("Ikke samme vare")

#b
navnEn = input("Første navn: ")
navnTo = input("Andre navn: ")
if navnEn.upper() < navnTo.upper():
    print("Navn i alfabetisk rekkefølge er: \n", navnEn, "\n", navnTo)
else:
    print("Navn i alfabetisk rekkefølge er: \n", navnTo, "\n", navnEn)
    
#c
#k er større en b
#Los Angeles
#New York
#druer