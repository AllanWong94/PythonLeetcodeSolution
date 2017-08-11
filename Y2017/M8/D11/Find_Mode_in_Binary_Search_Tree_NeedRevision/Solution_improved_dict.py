# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    # Runtime: 108ms Beats or equals to 40% (Fastest)

    def findMode(self, root):
        if not root:
            return []
        dict = {}
        self.traverse(root)
        modeCount = max(dict.values())
        return [k for k, v in dict.iteritems() if v==modeCount]

    def traverse(self, root):
        if root:
            dict[root.val] = dict.get(root.val, 0) + 1
            self.traverse(root.left)
            self.traverse(root.right)
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # Runtime: ms Beats or equals to %


t = TreeNode(2147483647)
solution = Solution()
print(solution.findMode(t))
