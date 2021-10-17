# t = 100
t = int(input())


def is_ok(r, g, b):
    if r == g:
        return r
    elif g == b:
        return g
    elif b == r:
        return r
    else:
        return 0


for i in range(t):
    cnt = 0
    memo = []
    r, g, b = list(map(int, input().split()))
    check = is_ok(r, g, b)
    diff = (g-r)//3 + 1
    if check:
        print(cnt + check)
        continue
    g -= diff
    b -= diff
    r += (diff * 2)
    cnt += diff

    diff = (b-g) // 3
    b -= (diff * 2)
    g += diff
    r += diff
    cnt += diff
    while True:
        r, g, b = sorted([r, g, b])
        if [r, g, b] in memo:
            print(-1)
            break
        else:
            memo.append([r, g, b])

        check = is_ok(r, g, b)
        if check:
            print(cnt + check)
            break

        diff = (g-r)//3 + 1
        g -= diff
        b -= diff
        r += (diff * 2)
        cnt += diff
