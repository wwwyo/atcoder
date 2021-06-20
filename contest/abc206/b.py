x = int(input())
day = 1
money = 0
while True:
    money += day
    if money >= x:
        print(day)
        break
    day+=1