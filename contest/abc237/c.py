

s = list(input())
start = 0
end = len(s)-1
is_a = True
while start < end:
    if s[start] != s[end]:
        if s[end] != 'a':
            is_a = False
        if not is_a:
            print('No')
            exit()
        end-=1
        continue
    start+=1
    end-=1
print('Yes')