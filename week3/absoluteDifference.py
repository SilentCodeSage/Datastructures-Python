def contracting(l):
    if len(l) == 1 or len(l) == 2 :
        return True
    differance = abs(l[1]-l[0])
    for i in range(2,len(l)):
        currentDifferance = abs(l[i]-l[i-1])
        if currentDifferance >= differance:
            return False
        else:
            differance = currentDifferance
    return True

print(contracting([10,7,3]))
