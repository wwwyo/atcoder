import math
a,b,c = map(int, input().split())

c = math.radians(c)
s = a*float(math.sin(c))*b/2
print(s)
print(a+b+float(math.sqrt(a**2+b**2-2*a*b*float(math.cos(c)))))
print(2*s/a)
