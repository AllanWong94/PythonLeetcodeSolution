# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    # Runtime: 112ms Beats or equals to 78%


    sum = 0

    def convertBST(self, root):
        return self.convert(root)

    def convert(self, root):
        if not root:
            return
        root.right = self.convert(root.right)

        root.val += self.sum
        self.sum = root.val
        root.left = self.convert(root.left)
        return root


t1 = TreeNode(5)
t2 = TreeNode(2)
t3 = TreeNode(13)
t1.left = t2
t1.right = t3
obj = Solution()
print(obj.convertBST(t1))
