from itertools import permutations

s,k = input().split()
s = list(s)
k = int(k)-1
ans = {}
for p in permutations(s, len(s)):
    ans[(''.join(p))] = 1

print(sorted(ans.keys())[k])



