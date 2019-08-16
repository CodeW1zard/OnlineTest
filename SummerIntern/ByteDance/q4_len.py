'''
绳子长度
'''
import sys

def sol(a, m):
    lo = 0
    hi = sum(a)/m+1
    mid = (lo+hi)/2
    while lo < hi+0.009:
        count = 0
        mid = lo + (hi-lo)/2
        for i in a:
            count += i//mid
        if count > m:
            lo = mid
        elif count < m:
            hi = mid
        else:
            break
    return round(mid*1000)/1000


if __name__ =='__main__':
    N, M = sys.stdin.readline().strip().split()
    N, M = int(N), int(M)

    a = list(map(int, sys.stdin.readline().strip().split()))
    print(sol(a, M))