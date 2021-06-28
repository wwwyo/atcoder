n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
cd = [list(map(int,input().split())) for _ in range(n)]

ab_distance = list(map(lambda x: x[0]**2+x[1]**2,ab))
cd_distance = list(map(lambda x: x[0]**2+x[1]**2,cd))
ab_dis_max = max(ab_distance)
cd_dis_max = max(cd_distance)
ab_max_idx = [i for i,_ in ab_distance if i == ab_dis_max]
cd_max_idx = [i for i,_ in cd_distance if i == cd_dis_max]

for i in ab_max_idx:
    ab_i = ab[i]
    for j in cd_max_idx:
        cd_j = cd[j]
        




