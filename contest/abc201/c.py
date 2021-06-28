s = input()
ans = 0
for i in range(10000):
    credit = "0"*(4-len(str(i)))+str(i)
    for j in range(10):
        if str(j) in credit and s[j] == 'x':
            break
        elif str(j) not in credit and s[j] == 'o':
            break
    else:
        ans+=1

print(ans)