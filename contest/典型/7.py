n = int(input())-1
a = list(map(int,input().split()))
a.sort()
# にぶたんで行ける
# import math
# print(math.log2(3 * (10 ** 5)) * 3 * (10 ** 5))
# 5 * 10^6

def binary_search(tree, x):
    left = 0
    right = len(tree)-1
    while left <= right:
        mid = (left + right) //2
        if tree[mid] > x:
            right = mid-1
        elif tree[mid] < x:
            left = mid+1
        else:
            return 0

    if 0 < mid < n:
        return min(abs(x-tree[mid-1]),abs(x-tree[mid]),abs(x-tree[mid+1]))
    elif 0 < mid:
        return min(abs(x-tree[mid-1]),abs(x-tree[mid]))
    elif mid < n:
        return min(abs(x-tree[mid]),abs(x-tree[mid+1]))
    else:
        return abs(x-tree[mid])


q = int(input())
for _ in range(q):
    b = int(input())
    print(binary_search(a,b))



