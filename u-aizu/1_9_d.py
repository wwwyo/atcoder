str = list(input())
n = int(input())
for _ in range(n):
    givens = input().split()
    com = givens[0]
    sta = int(givens[1])
    stop = int(givens[2])
    if com == 'print':
        print(''.join(str[sta:stop+1]))
    elif com == 'reverse':
        if len(str) != stop:
            str = str[:sta] + list(reversed(str[sta:stop+1])) + str[stop+1::]
        else:
            str = str[:sta] + list(reversed(str[sta:]))
    else:
        if len(str) != stop:
            str = str[:sta] + list(givens[3]) + str[stop+1::]
        else:
            str = str[:sta] + list(givens[3])