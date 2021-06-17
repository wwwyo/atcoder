w = input().lower()
str = input()
cnt = 0
while str.count("END_OF_TEXT") == 0:
    str = str.lower().split()
    cnt += str.count(w)
    str = input()

print(cnt)