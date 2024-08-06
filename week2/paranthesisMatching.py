def matched(s):
    count = 0
    for item in s:
        if(item == '('):
            count+=1
        elif(item == ')'):
            count-=1
            if(count < 0):
                return False
    return count == 0

print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))