# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode

# Runtime: 72ms Beats or equals to 88%

class Solution(object):
    def averageOfLevels(self, root):
        res=[]
        level=[root]
        while level:
            res.append(sum([i.val for i in level])/float(len(level)))
            next_level=[]
            for node in level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            level=next_level
        return res