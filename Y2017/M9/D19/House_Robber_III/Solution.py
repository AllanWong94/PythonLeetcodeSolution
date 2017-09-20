# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Reference: https://discuss.leetcode.com/topic/39700/c-java-python-explanation


# TLEed.
class Solution(object):
    def rob(self, root):
        return max(self.f1(root),self.f2(root))


        """
        :type root: TreeNode
        :rtype: int
        """

    def f1(self,root):
        if not root:
            return 0
        return max(self.f2(root),self.f2(root.left)+self.f2(root.right)+root.val)

    def f2(self, root):
        if not root:
            return 0
        return self.f1(root.left)+self.f1(root.right)


