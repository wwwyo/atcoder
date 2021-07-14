def split_list(l,n):
    for idx in range(0, len(l), n):
        yield l[idx:idx+n]

s = input()
l = list(map(int,list(s)))
cnt = int(s)

for div in range(1,len(l)+1):
    cnt+=sum(split_list(l,div))
print(cnt)

