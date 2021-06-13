n = int(input())
An = list(map(int, input().split()))
An = An[::-1]

for i, val in enumerate(An):
        print("{}".format(val), end = " " if i != (n-1) else None)