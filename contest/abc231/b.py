import collections
n = int(input())
s = {}
for _ in range(n):
    name = input()
    if s.get(name):
        s[name]+=1
    else:
        s[name] = 1
print(max(s,key=s.get))
