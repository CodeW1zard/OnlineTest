import sys


def sol(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0][1]
    num_neg = 0
    a.sort()
    for tree in a:
        if tree[0] < 0:
            num_neg += 1
        else:
            break
    num_pos = len(a) - num_neg
    m = min(num_pos, num_neg)

    res = sum(x[1] for x in a[num_neg - m:num_neg + m])
    if num_neg == num_pos:
        return res
    elif num_neg > num_pos:
        return res + a[num_neg - m - 1][1]
    else:
        return res + a[num_neg + m][1]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a = []
    i = 0
    for line in sys.stdin:
        tree = list(map(int, line.strip().split()))
        a.append(tree)
        i += 1
        if i == n:
            break
    print(sol(a))
