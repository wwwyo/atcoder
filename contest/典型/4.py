h,w = map(int,input().split())
# 行 + 列 - 自分
sum_row = [0] * h
sum_column = [0] * w
lst = []

for i in range(h):
    a = list(map(int,input().split()))
    lst.append(a)
    sum_row[i] = sum(a)
    for j in range(w):
        sum_column[j] += a[j]

for i in range(h):
    for j in range(w):
        if j == w-1:
            end = "\n"
        else:
            end = " "
        print(sum_row[i] + sum_column[j] - lst[i][j],end=end)

