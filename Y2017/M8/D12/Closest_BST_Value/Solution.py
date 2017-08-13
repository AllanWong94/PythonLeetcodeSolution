# Runtime: 69ms=>59 Beats or equals to 21%=>55%






# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    def closestValue(self, root, target):
        return self.helper(root,target,root.val)

        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

    def helper(self,root,target,temp):
        if abs(temp - target) > abs(root.val - target):
            temp = root.val
        if root.val > target and root.left:
            return self.helper(root.left, target,temp)
        elif root.val < target and root.right:
            return self.helper(root.right, target,temp)
        return temp

    # Runtime:52ms Fastest.
    # def closestValue(self, root, target):
    #     """
    #     :type root: TreeNode
    #     :type target: float
    #     :rtype: int
    #     """
    #     a = root.val
    #
    #     kid = root.left if root.val > target else root.right
    #
    #     if not kid:
    #         return a
    #
    #     b = self.closestValue(kid, target)
    #
    #     if abs(a - target) > abs(b - target):
    #         return b
    #     else:
    #         return a


t=TreeNode(2147483647)

solution = Solution()
print(solution.closestValue(t,0.0))

