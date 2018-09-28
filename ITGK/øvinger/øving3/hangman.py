hemmelig_ord = input("Skriv inn det hemmelige ordet: ")
antall_liv = int(input("Hvor mange forsøk får brukeren? "))
hvorMangePoeng = len(hemmelig_ord)

while True:
    brukerord = input("Gjett en bokstav: ")
    if brukerord in hemmelig_ord:
        print("Riktig!")
        hvorMangePoeng = hvorMangePoeng - 1
    else:
        antall_liv = antall_liv - 1
        print("Feil! Du har",antall_liv,"liv igjen.")

    if hvorMangePoeng == 0:
        print("Du vant! Ordet var",hemmelig_ord)
        break
    elif antall_liv == 0:
        print("Du tapte!")
        break

    