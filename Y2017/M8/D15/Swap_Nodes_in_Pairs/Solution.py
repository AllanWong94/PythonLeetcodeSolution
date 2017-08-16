# Runtime: 32ms Beats or equals to 99%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Y2017.ListNode import ListNode


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        sentinel = ListNode(-1)
        pointer = sentinel
        while head and head.next:
            prev, next, next_head = head, head.next, head.next.next
            prev.next = next.next = None
            pointer.next = next
            pointer.next.next = prev
            head, pointer = next_head, pointer.next.next
        if head:
            pointer.next = head
        return sentinel.next


nums = [1, 2]
head = ListNode(nums[0])
pointer = head
for i in range(1, len(nums)):
    pointer.next = ListNode(nums[i])
    pointer = pointer.next

obj = Solution()
print(obj.swapPairs(head))
print("done")
