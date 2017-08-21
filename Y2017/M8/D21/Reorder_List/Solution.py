# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Y2017.ListNode import ListNode


class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        walker = runner = head
        while runner.next and runner.next.next:
            walker, runner = walker.next, runner.next.next

        temp = walker.next
        walker.next = None
        walker = temp
        sentinel_even = ListNode(-1)
        while walker:
            next_node = walker.next
            walker.next = sentinel_even.next
            sentinel_even.next = walker
            walker = next_node
        odd_head, even_head = head.next, sentinel_even.next
        pointer = head
        head.next = None
        nexteven = even_head.next
        even_head.next = None
        pointer.next = even_head
        even_head = nexteven
        pointer = pointer.next
        while even_head:
            nextodd = odd_head.next
            odd_head.next = None
            pointer.next = odd_head
            odd_head = nextodd
            pointer = pointer.next
            nexteven = even_head.next
            even_head.next = None
            pointer.next = even_head
            even_head = nexteven
            pointer = pointer.next
        if odd_head:
            pointer.next = odd_head


"""
:type head: ListNode
:rtype: void Do not return anything, modify head in-place instead.
"""



# Runtime: 165ms Beats or equals to 72% One-time AC. Fastest




head=ListNode(1)
solution = Solution()
print(solution.reorderList(head))

