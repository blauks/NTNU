def overlapp(a,b,c,d):
    list1 = list(range(a,b+1))
    list2 = list(range(c,d+1))
    
    if bool(set(list1) & set(list2)):
        return True
    else:
        return False

while True:
    if overlapp(int(input("a ")),int(input("b ")),int(input("c ")),int(input("d "))):
        print("Nicern")
    else:
        print("Ikke nicern")
