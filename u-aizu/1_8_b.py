x = list(map(int, input()[0::]))
while x[0] != 0:
    print(sum(x))
    x = list(map(int, input()[0::]))