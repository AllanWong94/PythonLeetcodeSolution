# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Y2017.ListNode import ListNode


class Solution(object):
    # Runtime: 42ms Beats or equals to 91%
    def removeNthFromEnd(self, head, n):
        if n == self.helper(head, n):
            head=None
        return head

        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

    def helper(self, head, val):
        if not head:
            return 0
        temp = self.helper(head.next, val) + 1
        if temp == val + 1:
            head.next = head.next.next
        return temp
