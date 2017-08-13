# Runtime: 75ms Beats or equals to 80%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    def tree2str(self, t):
        res = ''
        if not t:
            return res
        res += str(t.val)
        if t.left or t.right:
            res += f'({self.tree2str(t.left)})'
            if t.right:
                res += f'({self.tree2str(t.right)})'
        return res
        """
        :type t: TreeNode
        :rtype: str
        """
    # Runtime:69ms
    # def tree2str(self, root):
    #     """
    #     :type t: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return ''
    #     elif root.left and root.right:
    #         return '{}({})({})'.format(root.val, self.tree2str(root.left), self.tree2str(root.right))
    #     elif root.left and not root.right:
    #         return '{}({})'.format(root.val, self.tree2str(root.left))
    #     elif not root.left and root.right:
    #         return '{}()({})'.format(root.val, self.tree2str(root.right))
    #     else:
    #         return '{}'.format(root.val)


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.right = t4

solution = Solution()
print(solution.tree2str(t1))
