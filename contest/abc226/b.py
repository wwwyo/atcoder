if __name__ == '__main__':
    # 2*10^5
    n = int(input())

    seq = {}
    cnt = 0
    for _ in range(n):
        la = input()

        if not seq.get(la):
            seq[la] = True
            cnt +=1
    print(cnt)
