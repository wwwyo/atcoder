a,b,c,d = map(int,list(input()))

if a == b == c == d:
    print('Weak')
    exit()
if (a+1)%10 == b and (b+1)%10 == c and (c+1)%10 == d:
    print('Weak')
    exit()
print('Strong')
