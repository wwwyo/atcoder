# 座標圧縮で課題2は通る

# w = 5 * 10 ^5
#  n = 2.5 * 10^5
w, n = map(int, input().split())

area = [0] * w
max_h = 0
for _ in range(n):
    l, r = map(lambda x: int(x)-1, input().split())
    max_h = max(area[l:r+1]) + 1
    for i in range(l, r+1):
        area[i] = max_h
    print(max_h)


class Segtree:
    def __init__(self, n, operator, identity):
        """
        n:データ配列のサイズ
        operator:演算子(モノイド)。関数オブジェクト
        identity:演算子に対応する単位元
        """
        nb = bin(n)[2:]  # ２進数に変換して戦闘の0bを取り除く
        # bitで1が立ってる数。これが1のときはちょうど2^nb.そうじゃないときは、2^nb<n<2^(nb+1)
        bc = sum([int(digit) for digit in nb])
        if bc == 1:  # 2^nbなら
            self.num_end_leaves = 2**(len(nb)-1)  # 最下段の葉っぱは2^nb個
        else:  # そうじゃないなら2^(nb+1)確保
            self.num_end_leaves = 2**(len(nb))

        self.array = [identity for i in range(
            self.num_end_leaves * 2)]  # 単位元で初期化

        self.identity = identity
        self.operator = operator
        # 後で使うので単位元と演算子を持っておく

    def update(self, x, val):
        """
        x:代入場所
        val:代入する値
        """
        actual_x = x+self.num_leaves
