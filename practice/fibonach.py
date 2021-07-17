f = [0,1]
for i in range(2,100):
    f.append(f[i-2] + f[i-1])
    print(f[i])
