# Runtime: 239ms Beats or equals to 92%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode
from Y2017.ListNode import ListNode


class Solution(object):
    def sortedListToBST(self, head):
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        def convert(a):
            if len(a)==0:
                return None
            if len(a)==1:
                return TreeNode(a[0])
            l=len(a)//2
            res=TreeNode(a[l])
            res.left=convert(a[:l])
            res.right=convert(a[l+1:])
            return res
        return convert(nums)

        """
        :type head: ListNode
        :rtype: TreeNode
        """

