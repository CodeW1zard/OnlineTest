import sys


def sol(n, ls, ds):
    if len(ds) == 1:
        print(ds[0])
        return
    z = sorted(list(zip(ls, ds)), reverse=True)
    i = 0
    res = 0
    while i < len(z):
        tmp = 0
        count = 1
        while z[i + 1][0] == z[i][0]:
            tmp += z[i][1]
            i += 1
            count += 1
        tmp += z[i][1]
        if count > n // 2:
            print(res)
            return
        n -= count
        res += tmp
    print(res)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    ls = list(map(int, sys.stdin.readline().strip().split()))
    ds = list(map(int, sys.stdin.readline().strip().split()))
    sol(n, ls, ds)
