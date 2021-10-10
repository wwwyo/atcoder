# m = 100
n,m = map(int,input().split())
a = [list(input()) for _ in range(2 * n)]


def is_left_win(x,y):
    if x == y:
        return 0
    elif x == 'G' and y == 'C' or x == 'C' and y == 'P' or x == 'P' and y == 'G':
        return 1
    else:
        return -1

# 順位は勝数
# 順位はiが若い順
# 2k-1 vs 2k

# 勝数,idx
rank = [[0,-i] for i in range(2 * n)]


for i in range(m):
    for j in range(n):
        x = a[-rank[2*j][1]][i]
        y = a[-rank[2*j+1][1]][i]
        res = is_left_win(x,y)
        # print(res)
        if res == 0:
            continue
        elif res == 1:
            rank[2*j][0]+=1
        else:
            rank[2*j+1][0]+=1
    # print(rank)
    rank.sort(reverse=True)
for i in rank:
    print((-i[1])+1)