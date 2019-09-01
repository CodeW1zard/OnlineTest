'''
n种类， m金钱
w1, w2, ... wn
v1, v2, ... vn

sum (x-wi)*vi <= m

'''
import sys

def solve(n, m, ws, vs):
    wmin = min(ws)
    ws = [w - wmin for w in ws]
    inds = sorted(range(n), key=lambda x:ws[x])
    cnt = 0
    incre = 0
    i = 0
    while m > 0:
        while cnt < ws[inds[i]]:
            if m < incre:
                print(cnt+wmin)
                return
            tmp = min(m // incre, ws[inds[i]]-cnt)
            m -= tmp * incre
            cnt += tmp

        if i < n:
            while cnt >= ws[inds[i]]:
                incre += vs[inds[i]]
                i += 1
                if i == n:
                    break
        if i == n:
            break
    cnt += m // incre + wmin
    print(cnt)
    return



if __name__ == '__main__':
    n, m = sys.stdin.readline().strip().split()
    n = int(n)
    m = int(m)
    ws = sys.stdin.readline().strip().split()
    vs = sys.stdin.readline().strip().split()
    ws = list(map(int, ws))
    vs = list(map(int, vs))
    solve(n, m, ws, vs)