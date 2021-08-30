n,m = map(int,input().split())
A = []
top_colors = {}

# 同じ色が見つかった玉
stack = []
for i in range(m):
    k = int(input())
    a = list(map(int,input().split()))[::-1]
    A.append(a)
    if a[-1] in top_colors:
        stack.append((top_colors[a[-1]], i))
    else:
        top_colors[a[-1]] = i

while stack:
    # そろっている筒のidx
    i, j = stack.pop()

    for k in (i,j):
        A[k].pop()
        if A[k] and A[k][-1] in top_colors:
            stack.append((top_colors[A[k][-1]], k))
        elif A[k]:
            top_colors[A[k][-1]] = k


if any(a for a in A):
    print('No')
else:
    print('Yes')
