# max(q) = 10^5
from collections import deque
q = int(input())
cards = deque()
for _ in range(q):
    t,x = map(int,input().split())
    if t == 1:
        cards.appendleft(x)
    elif t == 2:
        cards.append(x)
    elif t == 3:
        print(cards[x-1])

