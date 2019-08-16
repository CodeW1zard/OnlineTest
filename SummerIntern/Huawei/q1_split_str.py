import sys


def sol(n, a):
    outs = []
    for i in range(n):
        outs.extend(split(a[i]))
    outs.sort()
    print(" ".join(outs))


def split(s):
    out = []
    k, r = len(s) // 8, len(s) % 8
    for i in range(k):
        out.append(s[:8 * k])
    if not r:
        return out
    else:
        out.append(s[8 * k:] + (8 - r) * "0")
        return out


if __name__ == '__main__':
    inputs = list(sys.stdin.readline().strip().split())
    n = int(inputs[0])
    a = inputs[1:]
    sol(n, a)
