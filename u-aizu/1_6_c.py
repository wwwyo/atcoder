
sep =  "####################"
ans = [[[0 for i in range(10)] for j in range(3)] for k in range(4) ]

n = int(input())
for i in range(n):
	info = list(map(int, input().split()))
	ans[info[0]-1][info[1] -1][info[2]-1] += info[3]


for index, bu in enumerate(ans):
	for fl in bu:
		print(" "+" ".join(map(str, fl)))
	if index == 3:
		break
	print(sep)

