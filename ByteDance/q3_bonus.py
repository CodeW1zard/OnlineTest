import sys

def slope(a):
    n = len(a)
    if n==1 or a[1] == a[0]:
        return 0, 0
    elif a[1] > a[0]:
        i = 1
        while i+1 < n and a[i+1] > a[i]:
            i += 1
        return 1, i
    else:
        i = 1
        while i+1 < n and a[i+1] < a[i]:
            i += 1
        return -1, i

def solve(a):
    n = len(a)
    if n == 1:
        print(100)
        return

    i = 0
    bonus = [100] * n
    while i < n:
        flag, d = slope(a[i:])
        if not flag:
            i += 1
            continue
        if flag == 1:
            for j in range(d+1):
                bonus[i+j] = max(bonus[i+j], (j+1) * 100)
        elif flag == -1:
            for j in range(d+1):
                bonus[i+j] = max(bonus[i+j], (d+1-j) * 100)
        i += d
    print(sum(bonus))

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    solve(a)




