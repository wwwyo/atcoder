from collections import deque
# 10^5
n,m = map(int,input().split())
friends = [{} for _ in range(n)]

# 全部2か=>false
# 全部2以下か
def bfs(start,visited):
    is_circle = True
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.pop()
        len_ = len(friends[current])
        if len_ > 2:
            return False
        if len_ < 2:
            is_circle = False
        for next in friends[current]:
            if visited.get(next):
                continue
            visited[next] = True
            queue.append(next)

    if is_circle:
        return False
    else:
        return True

for _ in range(m):
    a,b = map(lambda x: int(x)-1,input().split())
    friends[a][b] = 1
    friends[b][a] = 1

visited = {}
for i in range(n):
    if not visited.get(i):
        if not bfs(i,visited):
            print('No')
            exit()
print('Yes')

# 円になってたら除外

# for friend in friends:
#     if len(friend)>2:
#         print('No')
#         exit()
#     if len(friend) < 2:
#         is_circle = False
# if is_circle:
#     print('No')
# else:
#     print('Yes')
