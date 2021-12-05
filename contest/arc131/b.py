# # 700
# h,w = map(int,input().split())
# colors = []
# for _ in range(h):
#     # 1~5
#     colors.append(list(map(lambda x: int(x) if x != '.' else 0,list(input()))))

# def paintColor(i,j):
#     d = [[0,1],[1,0],[-1,0],[0,-1]]
#     option = set([1,2,3,4,5])
#     for dx,dy in d:
#         x = dx + i
#         y = dy + j
#         if not(0<= x <h and 0 <= y < w): continue
#         if not colors[x][y]: continue
#         option -= {colors[x][y]}
#     option = list(option)
#     for dx,dy in d:
#         x = dx+i
#         y = dy+j
#         if not(0<= x <h and 0 <= y < w): continue
#         if not colors[x][y]: continue
#         colors[x][y] = option.pop()


# # 上下左右の色のマスが重ならない

# for i in range(h):
#     for j in range(w):
#         if (colors[i][j]): continue
#         color = paintColor(i,j)

# for i in range(h):
#     print(*colors[i])





# 700
h,w = map(int,input().split())
colors = []
for _ in range(h):
    # 1~5
    colors.append(list(map(lambda x: int(x) if x != '.' else 0,list(input()))))

def selectColor(i,j):
    d = [[0,1],[1,0],[-1,0],[0,-1]]
    option = set([1,2,3,4,5])
    for dx,dy in d:
        x = dx + i
        y = dy + j
        if not(0<= x <h and 0 <= y < w): continue
        if not colors[x][y]: continue
        option -= {colors[x][y]}
    return list(option)[0]



# 上下左右の色のマスが重ならない

for i in range(h):
    for j in range(w):
        if (colors[i][j]): continue
        color = selectColor(i,j)
        colors[i][j] = color

for i in range(h):
    print(''.join(map(str,colors[i])))





