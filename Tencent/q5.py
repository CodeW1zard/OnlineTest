'''

'''
import sys

def solve(dp, n):
    dpmin = [[x[0], x[1], x[2]] for x in dp]
    for i in range(1, n):
        if dp[i][0]:
            dp[i][0] += max(dp[i-1][:2])
            dpmin[i][0] += min(dpmin[i-1][:-2])
        else:
            dp[i][0] = max(-min(dp[i-1][:2]), -min(dpmin[i-1][:2]))
            dpmin[i][0] = min(-max(dp[i-1][:2]), -max(dpmin[i-1][:2]))
        if dp[i][1]:
            dp[i][1] += max(dp[i-1])
            dpmin[i][1] += min(dpmin[i-1])
        else:
            dp[i][1] = max(-min(dp[i-1]), -min(dp[i-1]))
            dpmin[i][1] = min(-max(dp[i-1]), -max(dpmin[i-1]))
        if dp[i][2]:
            dp[i][2] += max(dp[i-1][-2:])
            dpmin[i][2] += min(dpmin[i-1][-2:])
        else:
            dp[i][2] = max(-min(dp[i-1][-2:]), -min(dpmin[i-1][-2:]))
            dpmin[i][2] = min(-max(dp[i-1][-2:]), -max(dpmin[i-1][-2:]))
    return max(dp[-1])

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    dp = []
    for i in range(n):
        dp.append(list(map(int, sys.stdin.readline().strip().split())))
    print(solve(dp, n))
