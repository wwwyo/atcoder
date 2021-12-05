# 10^8
a = input()
b_origin = int(input())
b = str(b_origin / 2).replace('.','')[:9]
b = int(b)
if str(b_origin) in str(2 * b):
    print(a+'0'+str(b))
else:
    while True:
        b+=1

"""
xを探す
x 連続する文字列としてa
2x b
"""
