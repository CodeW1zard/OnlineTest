'''
修复字符串
'''
import sys


def sol(s):
    if len(s) == 3:
        if check_three(s, 0):
            return s[:-1]
        else:
            return s
    elif len(s) == 4:
        if check_four(s, 0):
            return s[:-1]
        else:
            return s

    cs = list(s)
    i = 0
    while i < len(cs) - 2:
        if check_three(cs, i):
            cs.pop(i + 2)
            continue
        try:
            if check_four(cs, i):
                cs.pop(i + 3)
                continue
        except:
            if i == len(cs)-2:
                break
        i += 1
    return ''.join(cs)


def check_three(a, i):
    return a[i] == a[i + 1] and a[i + 1] == a[i + 2]


def check_four(a, i):
    return a[i] == a[i + 1] and a[i + 2] == a[i + 3]


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    ss = []
    for i in range(N):
        s = sys.stdin.readline().strip()
        ss.append(sol(s))

    for i in range(N):
        print(ss[i])
