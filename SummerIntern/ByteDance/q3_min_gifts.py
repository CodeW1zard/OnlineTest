'''
分配奖品最小数量
'''
import sys


def sol(scores):
    if len(scores) == 1:
        return 1
    if len(scores) == 2:
        return 3 if scores[0] != scores[1] else 2

    def left(i):
        if i == 0:
            return len(scores) - 1
        return i - 1

    def right(i):
        if i == len(scores) - 1:
            return 0
        return i + 1

    dp = [1 for _ in scores]
    # flag = True
    # while flag:
    #     flag = False
    #     for i in range(len(dp)):
    #         prev = dp[i]
    #         if scores[i] > scores[left(i)]:
    #             dp[i] = max(dp[i], dp[left(i)] + 1)
    #         if scores[i] > scores[right(i)]:
    #             dp[i] = max(dp[i], dp[right(i)] + 1)
    #         if prev != dp[i]:
    #             flag = True
    # m = scores[0]+1
    # for i, sc in enumerate(scores):
    #     if sc < m:
    #         m = sc
    #         ind = i

    # for i in range(len(dp)):
    #     if scores[i] < scores[right(i)]:
    #         dp[right(i)] = dp[i] + 1
    # res = 0
    # for i in range(len(dp)-1, -1, -1):
    #     if scores[i] < scores[left(i)] and dp[left(i)] < dp[i]+1:
    #         dp[left(i)] = dp[i]+1
    #     res += dp[left(i)]
    i = 0
    for j in range(len(dp)):
        if scores[i] > scores[left(i)]:
            dp[i] = max(dp[i], dp[left(i)] + 1)
        if scores[i] > scores[right(i)]:
            dp[i] = max(dp[i], dp[right(i)] + 1)
        i = left(i)
    i = 1
    for j in range(len(dp)):
        if scores[i] > scores[left(i)]:
            dp[i] = max(dp[i], dp[left(i)] + 1)
        if scores[i] > scores[right(i)]:
            dp[i] = max(dp[i], dp[right(i)] + 1)
        i = right(i)

    return sum(dp)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    nums = []
    for i in range(N):
        n = int(sys.stdin.readline().strip())
        scores = list(map(int, sys.stdin.readline().strip().split(' ')))
        nums.append(sol(scores))

    for num in nums:
        print(num)
