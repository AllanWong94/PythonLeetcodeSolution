# Runtime: 202ms Beats or equals to 12%



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left,right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left,root.right))
        return root if left and right else left or right

    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    # Runtime: 86ms
    # Iterative is much much faster than Recursive!
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     while root:
    #         if not root or root == p or root == q:
    #             return root
    #
    #         if self.check(p, q):
    #             return p
    #         if self.check(q, p):
    #             return q
    #
    #         if self.check(root.left, p) and self.check(root.left, q):
    #             root = root.left
    #
    #         if self.check(root.right, p) and self.check(root.right, q):
    #             root = root.right
    #         else:
    #             return root
    #
    # def check(self, mother, child):
    #     if mother:
    #         if mother == child:
    #             return True
    #         else:
    #             return self.check(mother.left, child) or self.check(mother.right, child)
    #     return False


t1 = TreeNode(-1)
t2 = TreeNode(0)
t3 = TreeNode(3)
t4 = TreeNode(-2)
t5 = TreeNode(4)
t6 = TreeNode(8)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t4.left = t6






solution = Solution()
print(solution.lowestCommonAncestor(t1, t5, t6))
