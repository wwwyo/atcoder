
# 10**3
# a-z,(,)
def isInt(s):
    try:
        int(s)
        return True
    except:
        return False

def toInt(s):
    return ord(s) - 97

def toAlpha(i):
    return chr(i+97)

def removeFrom(counts):
    while counts:
        last = counts.pop()
        if last == '*':
            break
    else:
        counts.append('1')


def main():
    alphas = [0] * 26
    counts = ['1']
    s = list(input())
    prev_int = False
    cnt = 0
    for i in range(len(s)):
        if isInt(s[i]):
            if not prev_int:
                counts.append('*')
            counts.append(s[i])
        elif s[i] == '(':
            pass
        elif s[i] == ')':
            removeFrom(counts)
        else:
            alphas[toInt(s[i])] += eval(''.join(counts))
            if prev_int:
                removeFrom(counts)

        prev_int = isInt(s[i])
    for i in range(len(alphas)):
        print(toAlpha(i), alphas[i])

if __name__ == '__main__':
    main()



