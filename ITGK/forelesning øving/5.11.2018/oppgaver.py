def seqSearch(lst, item):
    for el in lst:
        if el == item:
            return True
    
    return False

print(seqSearch(["a","b","c","d"],"x"))

def binSearch(liste, verdi, imin, imax):
    if imax < imin:
        return "ikke funnet verdi"
    else:
        midtpunkt = (imin+imax)//2
        if verdi < liste[midtpunkt]:
            return binSearch(liste,verdi,imin,midtpunkt-1)
        elif verdi > liste[midtpunkt]:
            return binSearch(liste,verdi,midtpunkt+1,imax)
        else:
            return midtpunkt

liste = [1,2,3,9,11,13,17,25,57,90]
print(binSearch(liste,57,0,9))
