def sumPrimes(l):
    total = 0
    for item in l:
        count = 0;
        for i in range(1,item+1):
            if(item % i == 0):
                count = count+1
        if(count == 2):
            total = total+item
    return total
        


print(sumPrimes([17,51,29,39]))
 