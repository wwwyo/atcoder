# 同じ値のものが欲しい
# 差が3離れているとok
def sameMod(a, b):
    if a % 3 == b % 3:
        return True
    else:
        return False


def calc(a, b):
    if a == b:
        return a
    elif a > b:
        return b + (a-b)
    elif a < b:
        return a + (b-a)


def expectOperation(r, g, b):
    ans = []
    if sameMod(r, g):
        ans.append(calc(r, g))
    if sameMod(g, b):
        ans.append(calc(g, b))
    if sameMod(b, r):
        ans.append(calc(b, r))
    if not ans:
        return -1
    else:
        return min(ans)


t = int(input())
for _ in range(t):
    r, g, b = map(int, input().split())
    ans = expectOperation(r, g, b)
    print(ans)
