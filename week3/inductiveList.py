def length(l):
    if l == []:
        return 0
    else:
        return 1 + length(l[1:])

list = [1,2,3];

print(list[1:])
print(length(list))