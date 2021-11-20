# 10^5
n,k = map(int,input().split())
# 300/1 4日
scores = []
for _ in range(n):
    score = sum(map(int,input().split()))
    scores.append(score)

split_score = sorted(scores,reverse=True)[k-1]
for i in range(n):
    if scores[i] + 300 >= split_score:
        print('Yes')
    else:
        print('No')