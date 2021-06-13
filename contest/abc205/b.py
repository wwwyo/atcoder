n = int(input())
An = list(map(int, input().split()))

if len(An) == len(set(An)):
    print('Yes')
else:
    print('No')
