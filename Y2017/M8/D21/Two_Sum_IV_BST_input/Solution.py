# Runtime: 122ms Beats or equals to 89% One-time AC! Fastest.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        values = set()
        return self.helper(root, k, values)

    def helper(self, root, k, values):
        if not root:
            return False
        if k - root.val in values:
            return True
        values.add(root.val)
        return self.helper(root.left, k, values) or self.helper(root.right, k, values)

        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """





t1=TreeNode(1)

solution = Solution()
print(solution.findTarget(t1,2))

