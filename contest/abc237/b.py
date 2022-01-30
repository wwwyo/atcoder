
# n = int(input())
# s = list(input())
# a = [0]
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


h,w = map(int,input().split())
a = []
for _ in range(h):
    a.append(list(map(int,input().split())))

for row in zip(*a):
    print(*row)