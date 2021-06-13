n, m = map(int, input().split())
N = [list(map(int, input().split())) for i in range(n)]
M = [int(input()) for k in range(m)]
for row in N:
	ans = 0
	for (el, col) in zip(row, M):
		ans += el * col

	print(int(ans))