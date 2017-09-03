# Runtime: 132ms=>122ms Beats or equals to 65%=>89% One-time AC!
# pop() of list is expensive!


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Y2017.ListNode import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1=num2=0
        while l1 is not None:
            num1=num1*10+l1.val
            l1=l1.next
        while l2 is not None:
            num2=num2*10+l2.val
            l2=l2.next
        res=[int(i) for i in str(num1+num2)]
        head=ListNode(res[0])
        ptr=1
        pointer=head
        while ptr<len(res):
            pointer.next=ListNode(res[ptr])
            pointer=pointer.next
            ptr+=1
        return head

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    # Runtime: 112ms
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     if l1 == None:
    #         return l2
    #     elif l2 == None:
    #         return l1
    #     val1, val2 = 0, 0
    #     while (l1 != None):
    #         val1 = l1.val + val1 * 10
    #         l1 = l1.next
    #
    #     while (l2 != None):
    #         val2 = l2.val + val2 * 10
    #         l2 = l2.next
    #
    #     sum = val1 + val2
    #     head = ListNode(0)
    #     while (sum != 0):
    #         v = sum % 10
    #         head.val = v
    #         node = ListNode(sum / 10)
    #         node.next = head
    #         head = node
    #         sum = sum / 10
    #     return head.next if (val1 + val2) != 0 else head



solution = Solution()
print(solution)
