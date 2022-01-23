from itertools import permutations
n = 5
for lst in permutations(range(2*n),2*n):
    print(lst)