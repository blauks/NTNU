flag09 = "c1f02bbd538384ebb72267d3024831ec"

xored = ""

def change_to_be_hex(str):
    return int(str,base=16)

def xor_two_str(str1,str2):
    a = change_to_be_hex(str1)
    b = change_to_be_hex(str2)
    return hex(a ^ b)

f = open("hashedPasswords.txt")

for line in f.readlines():
    if line[0:2] == flag09[0:2]:
        print(line)
        if xored != "":
            xored = xor_two_str(xored, line.strip())
        else:
            xored = line.strip()

f.close()
print(str(xored[2:]))