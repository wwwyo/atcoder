from collections import deque

# maxでnは20
n = int(input())

def isCorrect(ans):
    left = right = 0

    for i in ans:
        if i == '(':
            left += 1
        else:
            right += 1
        if right > left:
            return False
    else:
        if left == right:
            return True
    return False


if n % 2 != 0:
    print()
else:
    # bit全探索で右か左をgreedy
    # チェックを通ったら出す
    # 2 ** 20 * 20 = 10 ** 7
    # !辞書順で出す必要がある
    for i in range(2 ** n):
        ans = deque()
        for j in range(n):
            if i >> j & 1:
                ans.appendleft(')')
            else:
                ans.appendleft('(')
        if isCorrect(ans):
            # print(bin(i))
            print(''.join(ans))

