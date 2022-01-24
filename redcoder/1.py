


# 300
def main(n,x):
    global ans
    for i in range(1,n-1):
        for j in range(i+1, n):
            if j < x - (i + j) <= n:
                ans += 1
    print(ans)


if __name__ == '__main__':
    while True:
        ans = 0
        n,x = map(int,input().split())
        if n == 0 and x == 0:
            break
        main(n,x)
