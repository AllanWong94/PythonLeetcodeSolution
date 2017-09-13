# Runtime: 42ms Beats or equals to 95%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode




class Solution(object):
    def flatten(self, root):
        def helper(_root):
            if not _root:
                return None
            if not _root.left:
                temp=_root
                while temp and temp.right:
                    temp=helper(temp.right)
                return temp
            temp=helper(_root.left)
            temp.right=_root.right
            _root.right=_root.left
            _root.left=None
            while temp.right:
                temp=helper(temp.right)
            return temp
        helper(root)

    # def flatten(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: void Do not return anything, modify root in-place instead.
    #     """
    #     while root:
    #         if root.left and root.right:
    #             pt = root.left
    #             while pt.right:
    #                 pt = pt.right
    #             pt.right = root.right
    #
    #         if root.left:
    #             root.right = root.left
    #             root.left = None
    #
    #         root = root.right

t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t1.right=t2
t2.left=t3




solution = Solution()
solution.flatten(t1)
print()

