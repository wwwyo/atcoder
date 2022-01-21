

def convertTime_s(x):
    h,m,s = map(int,x.split(':'))
    return h*3600 + m * 60 + s

def main(n):
    dist = [0] * (3600*24+1)
    for _ in range(n):
        a,b = input().split()
        a_t = convertTime_s(a)
        b_t = convertTime_s(b)
        dist[a_t] += 1
        dist[b_t] -= 1
    ans = 0
    cnt = 0
    for t in dist:
        cnt += t
        ans = max(ans,cnt)
    print(ans)




if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        main(n)
