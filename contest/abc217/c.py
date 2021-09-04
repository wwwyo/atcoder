n = int(input())
p = list(map(int,input().split()))
lst = list(enumerate(p))
lst.sort(key=lambda x: x[1])

# print(q)
for i in lst:
    print(i[0]+1,end=' ')
