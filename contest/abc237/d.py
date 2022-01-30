
n = int(input())
s = list(input())
a = [0] * (n+1)
# bef = 0
# cnt = 0
# # 順番を入れてソート
# for i in range(n):
#     if s[i] == 'L':
#         if bef == 0:
#             a = [i+1] + a
#         else:
#             a = a[:bef] + [i+1] + a[bef:]
#     else:
#         if bef == cnt:
#             a = a + [i+1]
#         else:
#             a = a[:bef+1] + [i+1] + a[bef+1:]
#         bef+=1
#     cnt+=1
# print(*a)

l = -pow(2,n)
r = -l
# l,rの差分より小さい数
for i in range(n):
    if s[i] == 'L':
        r = a[i]
        a[i+1] = (l + a[i]) / 2
    else:
        l = a[i]
        a[i+1] = (a[i] + r) / 2

    # print(a)

ans = []
for i in list(sorted(enumerate(a), key=lambda x: x[1])):
    ans.append(i[0])
print(*ans)


