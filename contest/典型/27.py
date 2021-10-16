n = int(input())
memo = {}
for i in range(n):
    s = input()
    if memo.get(s):
        continue
    memo[s] = 1
    print(i+1)

# import bisect
#10 ** 5
# n = int(input())
# bin_tree = []
# len_ = 0
# for i in range(n):
#     s = input()
#     idx = bisect.bisect_left(bin_tree, s)
#     if idx < len_ and s == bin_tree[idx]:
#         continue

#     bin_tree.insert(idx, s)
#     len_ += 1
#     print(i+1)
