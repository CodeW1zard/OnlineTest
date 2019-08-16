import sys

def sol(n, k):
    if n == 1:
        return 1
    cnt = 0
    while k > 0:
        n = n - n//2
        cnt += 1
        k -= 1
        if n == 1:
            return cnt+1
    return cnt + n



if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().strip().split()))
    count = 0
    print(sol(N, K))
