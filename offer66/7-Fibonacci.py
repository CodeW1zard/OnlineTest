'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        p = [0, 1]
        for k in range(n-1):
            i = k % 2
            p[i] = sum(p)
        return p[i]

def test():
    sol = Solution()
    for i in range(1, 6):
        print(sol.Fibonacci(i))
