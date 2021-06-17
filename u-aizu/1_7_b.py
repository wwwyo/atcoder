n, x = map(int,input().split())

while not(n == x == 0):
	cnt = 0
	for i in range(1,n-1):
		for j in range(i+1, n):
			remain = x-i-j
			if j < remain <= n:
				cnt += 1
	print(cnt)
	n, x = map(int,input().split())