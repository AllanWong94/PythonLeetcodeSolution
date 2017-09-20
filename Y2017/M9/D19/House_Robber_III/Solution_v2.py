# Runtime: 76ms Beats or equals to 57%   Fastest.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Reference: https://discuss.leetcode.com/topic/39700/c-java-python-explanation


class Solution(object):
    def rob(self, root):
        return self.dfs(root)[0]

        """
        :type root: TreeNode
        :rtype: int
        """

    def dfs(self,root):
        if not root:
            return 0
        l=self.dfs(root.left)
        r=self.dfs(root.right)
        return [max(l[0]+r[0],l[1]+r[1]+root.val), l[0]+r[0]]

