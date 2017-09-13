# Runtime: 85ms Beats or equals to 60%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def kthSmallest(self, root, k):
        count=self.count_nodes(root.left)
        if k<=count:
            return self.kthSmallest(root.left,k)
        elif k>count+1:
            return self.kthSmallest(root.right,k-1-count)
        return root.val

        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
    def count_nodes(self, root):
        if not root:
            return 0
        return 1+self.count_nodes(root.left)+self.count_nodes(root.right)
