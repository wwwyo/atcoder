
import bisect

def main():
    l, q = map(int,input().split())
    lst = [0,l]
    for _ in [0]*q:
        c,x = map(int,input().split())
        if c == 1:
            bisect.insort(lst, x)
        else:
            idx = bisect.bisect_right(lst, x)
            print(lst[idx]-lst[idx-1])
            
            
            
def main():
    l, q = map(int,input().split())
    lst = [l]
    for _ in [0]*q:
        c,x = map(int,input().split())
        if c == 1:
            
        else:
            idx = bisect.bisect_right(lst, x)
            print(lst[idx]-lst[idx-1])

main()