#a, b, c
dagerTilReise = int(input("Hvor mange dager er det til du skal reise? "))
pris = 440
if dagerTilReise >= 14:
    minipris = input("Du kan få minipris, ønsker du dette? (kan ikke refunderes) Ja/Nei ")
    if minipris == "ja" or minipris == "Ja": 
        pris=199
        print("Du kan få minipris:", pris, "NOK")
    else:
        alder = int(input("Hvor gammel er du? "))
        if alder >= 60 or alder > 18 and alder < 30:
            print("På grunn av din alder får du rabatt!")
            pris = pris * 0.5
            print("Total:",pris,"NOK")
        else:
            print("Da får du fullpris:", pris, "NOK")
else:
    alder = int(input("Hvor gammel er du? "))

