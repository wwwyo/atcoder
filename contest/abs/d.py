n = int(input())
a = map(int,input().split())

ans = [len(bin(i)) - bin(i).rfind('1') - 1 for i in a]
print(min(ans))