s = list(input())
t = list(input())
cnt = 0
skip = False
for l in range(len(s)):
    i = s[l]
    j = t[l]
    if i != j:
        if l == len(s)-1:
            print('No')
            break
        if s[l+1] != j:
            print('No')
            break
        else:
            s[l],s[l+1] = s[l+1],s[l]
            cnt += 1

        if cnt >= 2:
            print('No')
            break
else:
    print('Yes')

