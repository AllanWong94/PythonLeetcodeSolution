# Runtime: 32ms Beats or equals to 98% One-time AC.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        res=[]
        self.dfs(root, res)
        return res
        """
        :type root: TreeNode
        :rtype: List[int]
        """

    def dfs(self,root, res):
        if not root:
            return
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)