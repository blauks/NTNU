def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def weekday_newyear(year):
    ukeDag = 0
    for x in range(1900,year):
        if ukeDag == 5 and is_leap_year(x):
            ukeDag = 0
        elif ukeDag == 6 and is_leap_year(x):
            ukeDag = 1
        elif ukeDag == 6:
            ukeDag = 0
        elif is_leap_year(x):
            ukeDag += 2
        else:
            ukeDag += 1
    
    return ukeDag

for d in range(1900,1920):
    print(d, end=' ')
    if weekday_newyear(d) == 0:
        print(" man")
    elif weekday_newyear(d) == 1:
        print(" tir")
    elif weekday_newyear(d) == 2:
        print(" ons")
    elif weekday_newyear(d) == 3:
        print(" tor")  
    elif weekday_newyear(d) == 4:
        print(" fre")
    elif weekday_newyear(d) == 5:
        print(" lor")
    else:
        print(" son")

def is_workday(day):
    if day < 5:
        return True
    else: 
        return False

def workdays_in_year(year):
    hvorMangeArbeidsdager = 0
    ukeDag = weekday_newyear(year)
    hvorMangeDager = 0

    if is_leap_year(year):
        hvorMangeDager = 366
    else:
        hvorMangeDager = 365

    for x in range(hvorMangeDager):
        if is_workday(ukeDag):
            hvorMangeArbeidsdager += 1
        elif ukeDag == 6:
            ukeDag = -1
        ukeDag += 1
    
    return hvorMangeArbeidsdager

for ad in range(1900,1920):
    print("Det var",workdays_in_year(ad),"arbeidsdager i",ad)


