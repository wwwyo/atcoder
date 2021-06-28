a = int(input()) +1 #10
b = int(input()) +1 #2
c = int(input()) +1 #1
x = int(input()) //50
cnt = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            sum = 10*i + 2*j + k
            if sum == x:
                cnt+=1

print(cnt)





