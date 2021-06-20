n = int(input())
left = 0
right = 0
for i in range(n):
    cards = list(map(list,input().split()))
    l_count = len(cards[0])
    r_count = len(cards[1])
    count = min(len(cards[0]), len(cards[1]))
    cnt = 0
    for (l,r) in zip(cards[0],cards[1]):
        cnt += 1
        if l > r:
            left += 3
            break
        elif l < r:
            right += 3
            break
        elif cnt == count:
            if l_count > r_count:
                left+=3
            elif l_count < r_count:
                right+=3
            else:
                left += 1
                right += 1
        else:
            continue

print(left, right)