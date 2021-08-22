n = int(input())

for i in range(70):
    if 2 ** i > n:
        print(i-1)
        break


