# Runtime: 39ms Beats or equals to 90% One-time AC!
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Y2017.ListNode import ListNode, generateListNode


class Solution(object):
    def partition(self, head, x):
        if not head:
            return None
        greater=ListNode(-1)
        smaller=ListNode(-1)
        ptr_g,ptr_s=greater,smaller
        cur=head
        while cur:
            next=cur.next
            cur.next=None
            if cur.val<x:
                ptr_s.next=cur
                ptr_s=cur
            else:
                ptr_g.next=cur
                ptr_g=cur
            cur=next
        ptr_s.next=greater.next
        return smaller.next




        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

num=[2,1,3]
head=generateListNode(num)






solution = Solution()
res=solution.partition(head,2)
print()


