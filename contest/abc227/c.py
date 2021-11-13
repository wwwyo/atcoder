
# n = int(input())
# ans = 0
# for i in range(1,int(n**(1/3))+10):
#     for j in range(i,int(pow(n/i,0.5))+10):
#         ans+= max(0,n//(i*j)-j+1)

# print(ans)


n = int(input())
ans = 0
for a in range(1,n+1):
    if a*a*a>n: break
    for b in range(a,n+1):
        if a * b * b > n:
            break
        ans+= n//a//b - b+1
print(ans)

#!  /意味不明