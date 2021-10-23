s = list(input())
n = len(s)

if s[n-2::] == ['e', 'r']:
    print('er')
else:
    print('ist')