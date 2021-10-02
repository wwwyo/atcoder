n = list(input())
ans = 0
for i in range(2 ** len(n)):
    a = []
    b = []
    for j in range(len(n)):
        if i >> j &1:
            a.append(int(n[len(n) -j-1]))
        else:
            b.append(int(n[len(n) -j-1]))
    if a == [] or b == []: continue
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = max(ans, (int(''.join(map(str,a))) * int(''.join(map(str,b)))))
print(ans)


