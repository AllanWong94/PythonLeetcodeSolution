# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    # Runtime: 135ms  Beats or equals to 39%
    # Reference: https://discuss.leetcode.com/topic/83455/java-recursive-o-n-time/2
    def convertBST(self, root):
        self.traversal(root)
        return root

    def traversal(self, root, val=0):
        if not root:
            return val
        right=self.traversal(root.right,val)
        left=self.traversal(root.left, root.val+right)
        root.val+=right
        return left

t1 = TreeNode(2)
t2 = TreeNode(0)
t3 = TreeNode(3)
t4 = TreeNode(-4)
t5 = TreeNode(1)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
obj = Solution()
print(obj.convertBST(t1))
