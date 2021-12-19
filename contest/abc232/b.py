
# 10^5
s = list(input())
t = list(input())

alpha = {}
for i in range(97,97+26):
    alpha[chr(i)] = i - 97

diff =   alpha[t[0]]-alpha[s[0]]
# print(diff)
if diff < 0:
    diff += 26
# print(diff)
# print(alpha)
for i in range(len(s)):
    if alpha[t[i]] != (alpha[s[i]] + diff) %26:
        print('No')
        exit()
print('Yes')
