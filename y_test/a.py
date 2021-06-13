n, amount_min = map(int, input().split())
amount_items = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for amount_item in amount_items:
	amount = amount_item[0]
	profit = amount_item[1]
	if amount >= amount_min:
		ans += profit
print(ans)

