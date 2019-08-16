import sys


def sol(a, k):
    a.sort()
    prev = 0
    i = 0
    while i < k:
        if i >= len(a):
            print(0)
        elif a[i] == prev:
            k += 1
        else:
            print(a[i] - prev)
            prev = a[i]
        i += 1


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().strip().split()))
    a = list(map(int, sys.stdin.readline().strip().split()))
    sol(a, K)
