a = list(input())
for i in range(2**3):
    array = ['-']*3
    for j in range(3):
        if (i >> j) & 1:
            array[2-j] = '+'
    formula = ''
    array.append('')
    for k,l in zip(a,array):
        formula+=(k+l)
    if eval(formula) == 7:
        print("{}=7".format(formula))
        exit()