a, b = map(int, input().split())
d = int(a/b)
r = int(a%b)
f = float(a/b)

print("{} {} {:.5f}".format(d, r, f))
