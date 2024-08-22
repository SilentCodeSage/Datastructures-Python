def onehop(l):
    c = []
    for item in l:
        end_element = item[1] 
        for value in l:
            if end_element == value[0] and item[0] != value[1]:  
                c.append((item[0], value[1]))

    return c
print(onehop([(2,3),(1,2)]))