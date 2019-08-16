import sys
def sol(n, a, b):
    n -= sum(a)
    i = 0
    j = 0
    while i < n and j < 3:
        if a[j] < b[j]:
            a[j] += 1
            i += 1
        else:
            j += 1
    print("%d %d %d" % (a[0], a[1], a[2]))


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    ms = []
    Ms = []
    for i, line in enumerate(sys.stdin):
        m, M = list(map(int, line.strip().split()))
        ms.append(m)
        Ms.append(M)
        if i == 2:
            break
    sol(n, ms, Ms)
