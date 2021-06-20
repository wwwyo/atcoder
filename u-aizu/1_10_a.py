import math
a, b, c, d = list(map(float,input().split()))
distance = math.sqrt(abs(d-b)**2 + (c-a)**2)
print("{:.6f}".format(distance))