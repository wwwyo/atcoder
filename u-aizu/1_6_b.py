import itertools
suits = ['S', 'H', 'C', 'D']
nums = range(1,14)
def str_join(arr):
	arr = ' '.join(map(str, arr))
	return arr

comb = list(map(str_join, list(itertools.product(suits, nums))))

n = int(input())
for i in range(n):
        a = input()
        comb.remove(a)

for value in comb:
	print(value)

