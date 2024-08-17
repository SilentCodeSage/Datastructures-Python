def leftrotate(m):
    
    result = []
    for i in range(len(m)):
        l = []
        for j in range(len(m)):
            l.append(m[j][len(m)-1-i])
        result.append(l);
    return result

print(leftrotate([[1,1,1],[2,2,2],[3,3,3]]))