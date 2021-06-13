# n, q = map(int, input().split())
# arr = list(range(10**18+1))
# An = map(int, input().split())
# for i in An:
#     arr.remove(i)
# length = len(arr)
# max = arr[length-1]

# for _ in range(q):
# 	ord = int(input())
# 	if ord <= length:
# 		print(arr[ord])
# 	else:
# 		print(max+(ord-length))