import itertools

# 8,32
n,m = map(int,input().split())
ab = [[] for _ in range(n)]
cd = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(lambda x: int(x)-1,input().split())
    ab[a].append(b)
    ab[b].append(a)
for _ in range(m):
    c,d = map(lambda x: int(x)-1,input().split())
    cd[c].append(d)
    cd[d].append(c)
for i in range(n):
    ab[i].sort()
    cd[i].sort()

def is_same(p):
    for i in range(n):
        for j in ab[i]:
            if not p[j] in cd[p[i]]:
                return False
    return True

# 8!通りのcdの置き換えを試してabと一致するかチェックする
for p in itertools.permutations(range(n), n):
    if is_same(p):
        print('Yes')
        exit()

print('No')
