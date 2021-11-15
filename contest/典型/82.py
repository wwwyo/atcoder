# 10^18
l,r = list(input().split())
l_int,r_int = int(l),int(r)
l_len,r_len = len(l),len(r)
mod = 10**9+7

sum_=0
for i in range(l_len,r_len+1):
    start = max(10**(i-1),l_int)
    end = min(int('9'*(i)),r_int)
    s = (start+end)*(end-start+1)//2
    sum_ = (sum_+ s*i) %mod
print(sum_)