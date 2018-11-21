def binarySearch(num,el):
    if len(num) == 0:
        return "Tom liste"
    else:   
        m = len(num) // 2
        if num[m] == el:
            return m 
        elif num[m] < el:
            i = binarySearch(num[m:],el)
            m += i
        elif num[m] > el:
            m = binarySearch(num[:m],el)   
        else:
            m = -float('inf')    


    return m
    

    
    

print(binarySearch([1,4,6,9,13,34,45,53,65,78],4))