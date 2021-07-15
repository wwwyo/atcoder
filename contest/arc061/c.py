s = list(input())
emp_len = len(s)-1
cnt=0
for i in range(2**emp_len):
    empty = ['']*emp_len
    for j in range(emp_len):
        if (i>>j) &1:
            empty[emp_len - j-1] = '+'
    formula = ''
    empty.append('')
    for k,l in zip(s, empty):
        formula+=k+l
    cnt+= eval(formula)
print(cnt)
