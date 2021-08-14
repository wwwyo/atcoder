s = ['H', '2B', '3B', 'HR']
for _ in range(4):
    a = input()
    if a in s:
        s.remove(a)
    else:
        print('No')
        exit()
print('Yes')