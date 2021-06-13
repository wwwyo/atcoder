ans = 0
for i in range(1, 100000000000000):
    ans += 1/i
    if ans >= 15:
        print(i)
        break
