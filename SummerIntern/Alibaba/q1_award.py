from __future__ import print_function
import sys


def solve(n, ps):
    n = min(n, 100)
    i = 0
    p = 0
    prev = 1
    cnt = 0
    while True:
        if cnt % 2 == 0:
            p += prev * ps[i]
        prev *= (1 - ps[i])
        cnt += 1
        i += 1
        if cnt == 100:
            break
        elif cnt % n == 0:
            i = 0
    print("%.4f" % p)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    ps = []
    for i in range(n):
        ps.append(float(sys.stdin.readline().strip()))
    solve(n, ps)
