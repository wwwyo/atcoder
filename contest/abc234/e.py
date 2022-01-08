
# 10**17
def toInt(lst):
        return int(''.join(map(str,lst)))

def is_correct(x):
    diff = int(x[0]) - int(x[1])
    for i in range(1,len(x)-1):
        if not diff == (int(x[i]) - int(x[i+1])):
            return False
    return True
def main(x):

    if len(x) == 1:
        print(toInt(x))
        exit()

    if int(x[0] * len(x)) >= toInt(x):
        ans = x[0] * len(x)
    else:
        if x[0] == 9:
            ans = '1' + '0' * len(x)
        else:
            ans = str(int(x[0])+1) * len(x)
    ans = int(ans)
    if len(x) >= 11:
        print(ans)
        exit()
    elif len(x) >= 6:
        lst = [9,8,7,6,5,4,3,2,1,0]
        for i in range(11-len(x)):
            ans_ = toInt(lst[i:i+len(x)+1])
            if ans_ >= toInt(x):
                ans = min(ans,ans_)
        print(ans)
        exit()
    else:
        for i in range(toInt(x),10**6):
            if is_correct(list(str(i))):
                print(min(ans,i))
                exit()
if __name__ == '__main__':
    # for i in range(1,10**17):
    #     print(i)
    #     main(list(str(i)))
    x = list(input())
    main(x)



"""
 1. 同じ数にする


"""