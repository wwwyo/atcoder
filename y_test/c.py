n, action_num = map(int, input().split())
motivation = input()

S_3 = motivation.count('SSS')
S_3_b = motivation.count('S.S')
S_2 = motivation.count('SS')
S_1 = motivation.count('S')
if S_3 != 0:
	motivation = motivation.replace('SSS', '...', action_num)
	action_num -= S_3

if (action_num >= 0) and (S_3_b != 0):
	motivation = motivation.replace('S.S', '...', action_num)
	action_num -= S_3_b

if (action_num >= 0) and (S_2 != 0):
	motivation = motivation.replace('SS', '..', action_num)
	action_num -= S_2

if action_num >= 0:
	motivation = motivation.replace('S', '.', action_num)

ans = motivation.count('.')
print(ans)
