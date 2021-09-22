n = list(input())
num = len(n)
if num == 1:
    print(int(n[0]))
elif n[1:] == ['9'] * (num-1):
    print(sum(map(int,n)))
else:
    print(int(n[0])-1 + 9*(num-1))