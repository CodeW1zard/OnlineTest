import sys

a = sys.stdin.readline().strip().split()
b = sys.stdin.readline().strip().split()
n = len(a)
oids = sorted(range(n), key=lambda x:a[x], reverse=True)

def solve(b, oids, st, res):
        _w = b[oids[st-1]]
        N = 0
        if st:
            for i in range(st, n):
                w = b[oids[i]]
                w_, n_ = solve(b, oids, i)
                if w + w_ > 7 * _w:
                    continue
                elif n_ > N:
                    N = n_
                    ww = w + w_
        else:
            for i in range(st, n):
                w_, n_ = solve(b, oids, i)
                if n_ > N:
                    N = n_
        return ww, 1 + st



print(solve(b, oids, ))



