import collections
n = int(input())
# 10 ** 5
# 全部46のmodで管理できる
mod = 46
a = collections.Counter(map(lambda x: int(x) % mod,input().split()))
b = collections.Counter(map(lambda x: int(x) % mod,input().split()))
c = collections.Counter(map(lambda x: int(x) % mod,input().split()))

cnt = 0
for a_v,a_n in a.items():
    for b_v,b_n in b.items():
        for c_v,c_n in c.items():
            if (a_v + b_v + c_v) %mod == 0:
                cnt += a_n*b_n*c_n

print(cnt)
