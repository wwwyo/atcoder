import numpy as np

def search(arr):
    top = len(arr)
    left = len(arr)
    for i in range(len(arr)):
        if '#' in arr[i]:
            top = i
            left = arr[i].index('#')
            return top, left

def is_correct(s, t, t_top, t_left):
    s_top, s_left = search(s)
    top = t_top - s_top
    left = t_left - s_left
    for i in range(len(s)):
        for j in range(len(s)):
            try:
                if s[i][j] == '#' and s[i][j] != t[i+top][j+left]:
                    return False
            except:
                return False
    return True


n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]
t_top, t_left = search(t)

if n == 1:
    print('Yes')
    exit()


for _ in range(4):
    # 回転
    if is_correct(s,t, t_top, t_left):
        s_top, s_left = search(s)
        if is_correct(t,s, s_top,s_left):
            print('Yes')
            break
    s = np.rot90(s).tolist()
else:
    print('No')

