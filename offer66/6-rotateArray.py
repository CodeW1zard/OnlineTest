'''
旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        lo = 0
        hi = len(rotateArray) - 1
        if not hi:
            return 0

        while lo <= hi:
            m = lo + (hi - lo) // 2
            if rotateArray[lo] < rotateArray[hi]:
                return rotateArray[lo]
            if rotateArray[m] > rotateArray[m+1]:
                return rotateArray[m+1]
            if rotateArray[m] < rotateArray[m-1]:
                return rotateArray[m]
            if rotateArray[m] > rotateArray[lo]:
                lo = m + 1
            else:
                hi = m - 1
        return 0

def test():
    sol = Solution()
    cases = [
        # [3, 4, 5, 1, 2],
        # [1, 2, 3, 4, 5],
        # [4, 5, 1, 2, 3],
        [2, 2, 3, 3, 1, 2]
    ]
    for case in cases:
        print(sol.minNumberInRotateArray(case))


#
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         # write code here
#         m = 0
#         n = len(rotateArray)
#         if not n:
#             return m
#         if rotateArray[0] < rotateArray[-1]:
#             return rotateArray[0]
#         lo = 0
#         hi = n - 1
#         while lo < hi:
#             p = lo + (hi - lo + 1) // 2
#
#             if p < hi-1 and rotateArray[p] > rotateArray[p+1]:
#                 return rotateArray[p+1]
#             elif p > lo and rotateArray[p-1] > rotateArray[p]:
#                 return rotateArray[p]
#
#             if rotateArray[p] > rotateArray[0]:
#                 lo = p + 1
#             else:
#                 hi = p - 1
#
#         return min(rotateArray[lo], rotateArray[hi])
