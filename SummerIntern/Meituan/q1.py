from sys import stdin
from collections import defaultdict


def solve(ma):
    m = len(ma)
    n = len(ma[0])

    count1 = defaultdict(int)
    count2 = defaultdict(int)
    count = [count1, count2]

    for k in range(m * n):
        i = k // n
        j = k % n
        ind = k % 2
        count[ind][ma[i][j]] += 1

    max1 = 0
    max2 = 0
    maxnum1 = 'no'
    maxnum2 = 'no'
    for k, v in count[0].items():
        if v > max1:
            max1 = v
            maxnum1 = k

    for k, v in count[1].items():
        if v > max2:
            max2 = v
            maxnum2 = k

    res = m * n
    if maxnum1 == maxnum2:
        if max2 + res % 2 > max1:
            res -= max2 + findSubMax(count[0], maxnum2)
        else:
            res -= max1 + findSubMax(count[1], maxnum1)
    else:
        res -= max1 + max2
    return res


def findSubMax(count, max_ind):
    submax = 0
    for k, v in count.items():
        if v > submax and k != max_ind:
            submax = v
    return submax


if __name__ == '__main__':
    m, n = list(map(int, stdin.readline().strip().split()))
    ma = []
    for _ in range(m):
        x = list(map(int, stdin.readline().strip().split()))
        ma.append(x)

    print(solve(ma))
