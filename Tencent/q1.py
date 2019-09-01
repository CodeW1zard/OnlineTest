import sys


def solve(a, n, k):
    if k >= n or n == 1:
        return sum(a)
    i = 1
    res = sum(a[:k])
    tmp = res
    while 0 < i < n - k + 1:
        tmp = tmp - a[i-1] + a[i+k-1]
        if tmp < res:
            res = tmp
        i += 1
    return res


if __name__ == '__main__':
    n, k = sys.stdin.readline().strip().split()
    n = int(n)
    k = int(k)
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(a, n, k))
