'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
class Solution:
    def Power(self, base, exponent):
        if not exponent:
            return 1
        if exponent < 0:
            base = 1 / base
            exponent = -exponent
        return self.mypower(base, exponent)

    def mypower(self, base, exponent):
        if exponent == 1:
            return base
        p = 1
        res = base
        while 2 * p < exponent:
            p *= 2
            res *= res
        return res * self.mypower(base, exponent - p)

def test():
    sol = Solution()
    cases = [
        (2, 4),
        (2, 7),
        (3, 2),
        (2, -3)
    ]
    for case in cases:
        print(sol.Power(*case))

