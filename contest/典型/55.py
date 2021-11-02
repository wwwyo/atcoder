import itertools
from collections import Counter
# max(n) = 100
n,p,q = map(int,input().split())

a = list(map(lambda i:int(i) %p,input().split()))
ans = 0

# a = Counter(a).items()

# if len(a_cnt) <= 5:

# for comb in itertools.combinations(a,5):
#     multiplication = 1
#     cnt_ = 1
#     for key,cnt in comb:
#         multiplication *=key
#         cnt_ *= cnt
#     # print(multiplication)
#     if multiplication % p == q:
#         ans += cnt_
# print(ans)




# for comb in itertools.combinations(list(range(n)),5):
#     multiplication = 1
#     for i in comb:
#         multiplication *= a[i] % p
#     if multiplication % p == q:
#         ans += 1
# print(ans)


for i in range(n-4):
    for j in range(i+1,n-3):
        for k in range(j+1,n-2):
            for l in range(k+1,n-1):
                for m in range(l+1,n):
                    multi = a[i] * a[j] % p * a[k] %p * a[l] %p * a[m] %p
                    if multi == q:
                        ans+=1
print(ans)



