'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

动态规划
f(0) = 1
f(1) = 1
f(2) = f(1) + f(0)
f(n) = f(n-1) + f(n-2)
链接：https://www.nowcoder.com/questionTerminal/8c82a5b80378478f9484d87d1c5f12a4?answerType=1&f=discussion

若楼梯阶级 n = n
跳 2 步到 n：剩下的是第 n - 2 步没跳，起始跳到第 n - 2 步设它为 pre2 种
跳 1 步到 n：剩下的是第 n - 1 步没跳，起始跳到第 n - 1 步设它为 pre1 种
同时可以发现第 n 阶的解法，只要用到 n - 1 和 n - 2 阶是多少，其他的不用考虑，因此用两个变量临时存下来即可

dp(i) = dp(i-2) + dp(i-1)
'''


class Solution:
    def jumpFloor(self, n):
        if n <= 1:
            return n
        p = [1, 1]
        for k in range(n-1):
            i = k % 2
            p[i] = sum(p)
        return p[i]