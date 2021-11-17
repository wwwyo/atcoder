# 10^12
# k = int(input())

# cnt = 0
# for a in range(1,k+1):
#     if a**3 > k:
#         break
#     for b in range(a,k+1):
#         if a * b * b > k:
#             break
#         if k % (a*b) == 0 and k //(a*b) >= b:
#             cnt+=1
# print(cnt)



# 約数列挙
def make_division(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n %i == 0:
            lower_divisors.append(i)
            if i != n//i:
                upper_divisors.append(n//i)
        i+=1
    return lower_divisors + upper_divisors[::-1]

k = int(input())
cnt = 0
div = make_division(k)
for i in range(len(div)):
    for j in range(i,len(div)):
        a,b = div[i],div[j]
        if k % (a * b) == 0 and k // (a*b) >= b:
            cnt += 1
print(cnt)
