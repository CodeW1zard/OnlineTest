'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
f(0) = 1
f(1) = f(0)
f(2) = f(0) + f(1) = 2 * f(1)
f(3) = f(0) + f(1) + f(2) = 2 * f(2)
...
f(n) = \sum_0^(n-1) f(i) = 2 * f(n-1)
'''

class Solution:
    def jumpFloorII(self, number):
        return 2 ** (number - 1)