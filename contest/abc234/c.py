# 10**18
k = int(input())
ans = ''
# 桁数
for i in range(len(bin(k))):
    if k >> i &1:
        ans += '2'
    else:
        ans += '0'
print(int(''.join(list(reversed(ans)))))





