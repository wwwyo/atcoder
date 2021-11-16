# 10^6
n = int(input())
s = list(input())


# start = 0
# cnt = 0
# for i in range(1,n):
#     if s[start] != s[i]:
#         back = n-i
#         front = i-start
#         cnt += (front*back)
#         start = i
# print(cnt)


#全通りから余事象を引く

cnt = n * (n+1)//2
start = 0
for i in range(1,n):
    if s[start] != s[i]:
        same_mark_len = i-start
        cnt -= (same_mark_len * (same_mark_len+1) // 2)
        start = i
cnt-=((n-start)*(n-start+1)//2)
print(cnt)