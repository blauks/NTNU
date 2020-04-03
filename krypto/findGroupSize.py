gruppe = []

mod = 78

x = 1

generator = 13

curNmbr = 0

while True:
    if generator**(x-1)%mod in gruppe:
        break
    gruppe.append(generator**(x)%mod)
    x += 1
    print(gruppe)

print(gruppe)
print(len(gruppe))