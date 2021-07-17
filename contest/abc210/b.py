n = int(input())
s = list(input())

idx = s.index('1')
if idx %2 == 0:
    print('Takahashi')
else:
    print('Aoki')