n = int(input())

ans = ''
for i in range(1, n+1):
	if i % 3 == 0:
		ans+= ' ' + str(i)
	elif '3' in str(i):
		ans+= ' ' + str(i) 
print(ans)