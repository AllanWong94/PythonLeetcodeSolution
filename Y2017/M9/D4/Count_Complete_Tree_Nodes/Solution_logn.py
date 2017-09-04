# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode

# Runtime: 172ms Beats or equals to 66%
# Reference: https://discuss.leetcode.com/topic/15533/concise-java-solutions-o-log-n-2
class Solution(object):
    def countNodes(self, root):
        def height(node):
            return -1 if not node else 1 + height(node.left)

        h = height(root)
        return 0 if h < 0 else (
        (1 << h) + self.countNodes(root.right) if height(root.right) == h - 1 else (1 << h - 1) + self.countNodes(
            root.left))

        """
        :type root: TreeNode
        :rtype: int
        """
