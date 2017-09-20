# Runtime: 48ms Beats or equals to 73% Fastest.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Y2017.ListNode import ListNode


class Solution(object):
    def rotateRight(self, head, k):
        self.pre = self.tail = None
        length=self.getPre(head,k)
        if not head or length == k:
            return head
        elif length<k:
            return self.rotateRight(head, k%length)
        else:
            self.tail.next = head
            next = self.pre.next
            self.pre.next = None
            return next
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

    def getPre(self, head, k):
        if not head:
            return 0
        else:
            tmp = self.getPre(head.next, k) + 1
            if tmp == 1:
                self.tail = head
            if tmp == k + 1:
                self.pre = head
            return tmp
