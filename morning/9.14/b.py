a1,a2,a3 = map(int,input().split())
# 0にしたい
a = 2*a2 - a1 - a3
# pattern1:0以下の時2を足す
k = max(0, (-a+1) // 2)
# pattern2:超えた分を-1
k += (a + 2 * k)


print(k)
# ポイント
# 漸化式を等式変換する
# 最終やりたいことを考える。今回はa を0にする
# 選択肢は-1or+2だったので住み分けができた