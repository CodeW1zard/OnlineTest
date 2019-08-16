'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
class Solution:
    def NumberOf1(self, n):
        cnt = 0
        flag = n > 0
        while n:
            n, cnt = n // 2, cnt + n % 2
        cnt += not flag
        return cnt


