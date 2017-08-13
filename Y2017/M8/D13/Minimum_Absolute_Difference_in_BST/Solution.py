# Runtime: 79ms Beats or equals to 97%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode

class Solution(object):
    values=[]
    def getMinimumDifference(self, root):
        self.traversal(root)
        values=self.values
        values.sort()
        margins=[values[i+1]-values[i] for i in range(len(values)-1)]
        return min(margins)
        """
        :type root: TreeNode
        :rtype: int
        """
    def traversal(self,root):
        if root:
            self.values.append(root.val)
            self.traversal(root.left)
            self.traversal(root.right)


t1=TreeNode(1)
t2=TreeNode(5)
t3=TreeNode(3)
t1.right=t2
t2.left=t3







solution = Solution()
print(solution.getMinimumDifference(t1))

