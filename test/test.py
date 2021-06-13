n = int(input())
array = list(map(int, input().split()))

array.sort()
print("{} {}".format(min(array), max(array)))
print(''.join(map(str, array)))