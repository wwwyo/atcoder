n,k = input().split()
k = int(k)

def convertFrom10Int(n,base):
    if n // base:
        return convertFrom10Int(n//base,base) + str(n % base)
    return str(n%base)

for _ in range(k):
    # 10進数に直す
    n_10 = int(n,8)
    # 9進数に変換
    n_9 = convertFrom10Int(n_10,9)
    # 8を5に変換
    n = n_9.replace('8','5')

print(n)
