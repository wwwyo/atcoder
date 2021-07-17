# URL(momoyama-usagi.com/entry/info-algo-dp)
# [カロリー, 値段]
sushi = [[],[80,120], [100,150],[70,140],[60,110],[70,100]]
limit = 300



limit //= 10
dp_table = [[0 for _ in range(limit+1)] for _ in range(len(sushi))]
sushi_len = len(sushi)

for len in range(1,len(sushi)):
    for lim in range(limit+1):
        if sushi[len][0]//10 > lim:
            dp_table[len][lim] = dp_table[len-1][lim]
        else:
            dp_table[len][lim] = max(dp_table[len-1][lim], dp_table[len-1][lim-(sushi[len][0]//10)] + sushi[len][1])

print(dp_table[sushi_len-1][limit])