s = ''.join(list(reversed(input())))
while 1:
    for i in ('maerd','esare', 'remaerd', 'resare'):
        if s.startswith(i):
            s = s[len(i)::]
            break
    else:
        print('NO')
        exit()
    if len(s) == 0:
        print('YES')
        break
