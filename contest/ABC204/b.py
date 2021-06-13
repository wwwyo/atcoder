n = int(input())
An = map(int, input().split())
count = 0
for i in An:
  if i > 10:
    count += i-10
print(count)

