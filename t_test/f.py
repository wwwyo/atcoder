a = 49
st = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
left = [st[0]]
right = []
cnt = 0
while a > 0:
	left.append(st[(cnt + (a)*4)%26])
	right.append(st[(cnt + a*2)%26])
	cnt += a * 4
	a-=2
 
 

right.reverse()
