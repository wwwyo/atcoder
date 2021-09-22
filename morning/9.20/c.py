# リストスライスは重い
n = int(input())
s = list(input())
ss = []

for i in s:
    ss.append(i)
    if len(ss) < 3:
        continue
    if ss[-3::] == ['f', 'o', 'x']:
        for _ in range(3):
            ss.pop()
print(len(ss))
