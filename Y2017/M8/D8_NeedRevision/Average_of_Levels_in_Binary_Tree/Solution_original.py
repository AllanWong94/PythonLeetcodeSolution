# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode

# Runtime: 79ms Beats or equals to 60%

class Solution(object):
    info=[]

    def averageOfLevels(self, root):
        self.helper(root,0)
        return [s/float(c) for s,c in self.info]
        """
        :type root: TreeNode
        :rtype: List[float]
        """

    def helper(self, root, level):
        if root:
            if level+1 > len(self.info):
                self.info.append([root.val,1])
            else:
                self.info[level][0] += root.val
                self.info[level][1] += 1
            self.helper(root.left, level + 1)
            self.helper(root.right, level + 1)


t1=TreeNode(5)
t2=TreeNode(2)
t3=TreeNode(-3)
t1.left=t2
t1.right=t3
obj=Solution()
print(obj.averageOfLevels(t1))