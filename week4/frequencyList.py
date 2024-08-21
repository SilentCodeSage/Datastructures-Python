def frequency(l):
    (minfreqlist,maxfreqlist) = ([],[])
    if l == []:
        return (minfreqlist,maxfreqlist)
    
    if len(l) == 1:
        (minfreqlist,maxfreqlist) = ([1],[1])
        return (minfreqlist,maxfreqlist)
    
    largest = max(abs(x) for x in l)

    hash = [0] * (largest + 1)
    
    for element in l:
        hash[abs(element)] +=1

    newLarge = 0
    for item in hash:
        if item > newLarge:
            newLarge = item

    secondnewLargest = newLarge
    for item in hash:
        if item < secondnewLargest and item > 0:
            secondnewLargest = item
    
    

    for i in range(0,len(hash)):
        if(hash[i] == newLarge):
            maxfreqlist.append(i)
        elif(hash[i] == secondnewLargest):
            minfreqlist.append(i)

    if secondnewLargest == newLarge:
        minfreqlist = maxfreqlist


    return (minfreqlist,maxfreqlist)


print(frequency([-12, -13, -13, -12, -12]))

    
