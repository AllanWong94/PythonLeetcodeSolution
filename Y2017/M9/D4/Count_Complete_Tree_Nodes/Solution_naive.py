# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode

#TLEed.
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)





        """
        :type root: TreeNode
        :rtype: int
        """
