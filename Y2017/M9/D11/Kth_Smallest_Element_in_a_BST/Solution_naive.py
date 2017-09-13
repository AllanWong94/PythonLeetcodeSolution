# Runtime: 102ms Beats or equals to 20% One-time AC.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def kthSmallest(self, root, k):
        self.store=[]
        self.helper(root)
        self.store.sort()
        return self.store[k-1]


        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
    def helper(self, root):
        if not root:
            return
        self.store.append(root.val)
        self.helper(root.left)
        self.helper(root.right)