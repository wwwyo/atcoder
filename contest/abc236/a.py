s = list(input())
a,b = map(lambda x: int(x)-1,input().split())
s[a],s[b] = s[b],s[a]
print(''.join(s))