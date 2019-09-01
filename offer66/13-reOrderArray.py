'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
[2, 4, 6, 1, 3, 8, 5, 7]
[1, 3, 5, 7, 2, 4, 6, 8]
'''
class Solution:
    '''
    类似具有稳定性的排序，考虑插入排序，
    向后遍历，每次和左边比较，若小则前移
    --->
    向后遍历，每次判断是否奇数，若是则左移
    '''
    @classmethod
    def reOrderArray(self, array):
        k = 0
        for i, x in enumerate(array):
            if x % 2:
                j = i
                while j > k:
                    array[j], array[j-1] = array[j-1], array[j]
                    j -= 1
                k += 1
        return array

def test():
    cases = [
        [2, 4, 6, 1, 3, 8, 5, 7]
    ]
    for case in cases:
        print(Solution.reOrderArray(case))
