
a = [1,0,5]
for i in range(32):
	a.append(a[i]+a[i+1]+a[i+2])

print(a[31])

