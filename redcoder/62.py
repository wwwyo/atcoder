
def warshallFloyd():
    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j],c[i][k] + c[k][j])


if __name__ == '__main__':
    # 全て1にする
    # 200
    h,w = map(int,input().split())
    c = []
    a = []
    for _ in range(10):
        c.append(list(map(int,input().split())))
    for _ in range(h):
        a.append(list(map(int,input().split())))
    warshallFloyd()
    ans = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == -1:
                continue
            ans += c[a[i][j]][1]
print(ans)





