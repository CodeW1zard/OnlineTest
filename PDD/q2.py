import sys

a = sys.stdin.readline().strip().split()
n = len(a)

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

res = []

def solve(a, k, res):
    if k == n:
        res.append(k)
        return
    i = k
    while i < n:
        if k and a[k-1][-1] == a[i][0]:
            swap(a, k, i)
            solve(a, k+1, res)
            swap(a, k, i)
        elif not k:
            swap(a, k, i)
            solve(a, k+1, res)
            swap(a, k, i)
        i += 1


solve(a, 0, res)
if res:
    print('true')
else:
    print('false')