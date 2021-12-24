# 10^4
n = int(input())
s = list(input())

# 実際は、高々10^3通りしか存在しない
# この10^3通りを貪欲で調べる

ans = 0
for k in range(10**3):
    # 0埋め
    current = 0
    tmp = list(f'{k:03}')
    for i in s:
        if i == tmp[current]:
            current+=1
        if current >=3:
            ans +=1
            break
print(ans)