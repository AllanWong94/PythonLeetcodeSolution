# Runtime: 32ms Beats or equals to 96% One-time AC.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        self.res=[]
        self.dfs(root)
        return self.res
        """
        :type root: TreeNode
        :rtype: List[int]
        """


    def dfs(self,root):
        if not root:
            return
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)