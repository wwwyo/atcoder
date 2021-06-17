r, c = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(r)]
col_sum = [0]*(c+1)
for row in rows:
    row_sum = 0
    for i in range(c):
        col_sum[i] += row[i]
        row_sum += row[i]
        print(row[i],end=' ')
    col_sum[c] += row_sum
    print(row_sum)
print(" ".join(map(str,col_sum)))