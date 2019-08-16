from __future__ import print_function
import sys


def solve(m, n, k):
    if k == 1:
        return 0
    cnt = 0
    for i in range(1, k):
        if i > m:
            continue
        tmp = func(m - 1, i - 1) / fac(i-1)
        for j in range(1, k - i + 1):
            if j > n:
                continue
            cnt += tmp * func(n - 1, j - 1)
    return int(cnt)


def fac(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def func(n, k):
    """
    n choose k
    """
    assert n >= k
    l = n - k
    res = 1
    for i in range(k + 1, n + 1):
        res *= i
    for i in range(1, l + 1):
        res /= i
    return res


if __name__ == '__main__':
    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    print(solve(m, n, k) % 10000)
