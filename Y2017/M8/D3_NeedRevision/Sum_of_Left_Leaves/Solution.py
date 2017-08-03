from Y2017 import TreeNode


class Solution(object):
    # Runtime: 39ms Beats or equals to 87% One-time AC!
    def sumOfLeftLeaves(self, root):
        self.result = 0
        self.helper(root,False)
        return self.result
        """
        :type root: TreeNode
        :rtype: int
        """

    def helper(self, root, leftleaf):
        if leftleaf and not root.left and not root.right:
            self.result += root.val
            return
        if root.left:
            self.helper(root.left, True)
        if root.right:
            self.helper(root.right, False)
