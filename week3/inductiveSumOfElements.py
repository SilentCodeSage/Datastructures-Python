def sum(l):
    if l == []:
        return 0
    else:
        return l[0] + sum(l[1:])

list = [1,2,3];

print(list[1:])
print(sum(list))