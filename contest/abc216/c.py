n = int(input())
print('A', end = '')
ans = []
for i in range(130):
    if n == 1:
        break
    if n % 2 == 0:
        n //= 2
        ans.append('B')
    else:
        n -= 1
        ans.append('A')
print(''.join(reversed(ans)))


