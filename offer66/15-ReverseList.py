"""
输入一个链表，反转链表后，输出新链表的表头。
1, 2, 3, 4, 5, 6
2, 1, 3, 4, 5, 6
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    @classmethod
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        dummy = ListNode(0)
        dummy.next = pHead
        node = pHead
        while node.next is not None:
            prev = dummy.next
            dummy.next = node.next
            node.next = node.next.next
            dummy.next.next = prev
        return dummy.next

def test():
    case = [i for i in range(1, 7)]
    head = ListNode(case[0])
    node = head
    for i in case[1:]:
        node.next = ListNode(i)
        node = node.next
    res = Solution.ReverseList(head)
    vals = []
    while res.next is not None:
        vals.append(res.val)
        res = res.next
    vals.append(res.val)
    print(vals)

