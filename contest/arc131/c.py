"""
2手後にゲームが終わるか

2手後にゲームが終わるとする
1手目に任意のiをとった時後手がゲームを終わらせるようなkを取る
i=>kを取る逆も成りたつ1手目k=>2手目i
このような組が成り立つのでN/2個存在する。
=>奇数だと成り立たない
偶数だと相手で終わる。
奇数だと自分で終わる
"""
# n = 10**5
n = int(input())
a = list(map(int,input().split()))

if n %2 == 1:
    print('Win')
    exit()

xor = a[0]
for i in range(1,n):
    xor ^=a[i]
for i in range(n):
    if xor^a[i] ==0:
        print('Win')
        break
else:
    print('Lose')
