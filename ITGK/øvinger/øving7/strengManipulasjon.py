def finnPlassering(s,s1):
    plasseringListe = []
    s = s.lower()
    s1 = s1.lower()
    for x in range(len(s1)):
        if s1[x:(x+len(s))] == s:
            plasseringListe.append(x)

    return plasseringListe

print(finnPlassering("is","Is this the real life? Is this just fantasy?"))

def endre(s,s1,s2):
    lista = finnPlassering(s,s1)
    streng = ""
    start = 0
    for x in lista:
        streng += s1[start:x]
        streng += s2
        start = x + len(s2)
    streng += s1[start:]
    return streng

print(endre("a","abc bac cba","1"))