while True:
    pos = input("Skriv inn en posisjon på sjakkbrettet: ")
    if len(pos) == 2:
        bokstav = pos[0]
        tall = int(pos[1])
        if bokstav >= "A" and bokstav <= "H" or bokstav >= "a" and bokstav <= "h":
            PeO = ord(bokstav) + tall
            if PeO%2==0:
                print("Svart")
            else:
                print("Hvit")  
        else:
            print("Feil input")
    else:
        print("Feil input")
