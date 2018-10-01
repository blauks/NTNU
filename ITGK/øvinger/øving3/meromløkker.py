antTast = 7
suma = 0

while antTast > 0:
    antTast = antTast-1
    tall = int(input("Skriv inn et heltall: "))
    suma = suma + tall

print(suma) 

tall1 = 0
tall2 = 0
sumb = 0
while sumb <= 1000:
    tall1 = tall1 + 1
    tall2 = tall2 + 1
    sumb = tall1*tall2
    print(sumb)

antallForsøk = 0
while True:
    svar = input("Hva er hovedstaden i Norge? ")
    antallForsøk = antallForsøk + 1
    if svar == "Oslo" or svar == "oslo": 
        print("Korrekt svar! Du brukte", antallForsøk, "forsøk!")
        break
    else:
        print("Feil svar, prøv igjen!")
