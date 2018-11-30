def load_bin(navn):
    innhold = ""
    try:
        fil = open(navn,"r")

        for linjer in fil:
            innhold += linjer.strip()

        fil.close()
    except:
        print("Error: could not find", navn)

    return innhold

#print(load_bin(input("")))

def bin_to_dec(binary):
    sumB = 0
    binary = binary[::-1] #for å reversere en streng 
    for x in range(len(binary)):
        if binary[x] == "1":
            sumB += 2**x

    return sumB

#print(bin_to_dec("101"))

def dec_to_char(dec):
    tegn = " ,.ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    if dec>=0 and dec <= 31:
        return tegn[dec]
    return None

#print(dec_to_char(5))

def bin_to_txt(binstring):
    x = 0
    streng = ""
    while x <= len(binstring):
        streng += dec_to_char(bin_to_dec(binstring[x:x+5]))
        x += 5

    return streng

print(bin_to_txt("101000010001101"))

