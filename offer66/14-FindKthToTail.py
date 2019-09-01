'''
输入一个链表，输出该链表中倒数第k个结点。
'''

class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None
        node1 = head
        node2 = head
        while node1.next is not None:
            node1 = node1.next
            k -= 1
            if k <= 0:
                node2 = node2.next
        # 若k > 链表长度 (node1只需要len-1次循环，k>len，故k-(len-1) > 1)
        if k > 1:
            return None
        return node2