import math
a,b,c = map(int,input().split())

# 浮動少数は誤差を生む
# b * log2(c) <=> log2(c ** b)
# a と c ** b
if a < c ** b:
    print('Yes')
else:
    print('No')