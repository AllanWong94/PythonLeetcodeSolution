# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    #oddly incorrect output for test case [2147483647].
    dict = {}

    def findMode(self, root):
        self.traverse(root)
        modeCount = max(self.dict.values())
        res = []
        for k in self.dict.keys():
            if self.dict[k] == modeCount:
                res.append(k)
        return res

    def traverse(self, root):
        if root:
            self.dict[root.val] = self.dict.get(root.val, 0) + 1
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
