n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

def calc(p,f=False):
    ans = 0
    arr=[]
    for i,j in zip(x,y):
        ans += abs(i-j)**p
        arr.append(abs(i-j))
    if f:
        return max(arr)
    else:
        print(float(ans**(1/p)))

calc(1)
calc(2)
calc(3)
print(calc(1,True))

