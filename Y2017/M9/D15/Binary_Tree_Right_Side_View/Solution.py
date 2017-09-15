# Runtime: 38ms Beats or equals to 86%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    def rightSideView(self, root):
        self.count=0
        res=[]
        def helper(root,depth):
            if not root:
                return
            if self.count<depth:
                res.append(root.val)
                self.count+=1
            helper(root.right, depth+1)
            helper(root.left, depth+1)
        helper(root,1)
        return res
        """
        :type root: TreeNode
        :rtype: List[int]
        """


t=[TreeNode(i) for i in range(1,5)]
t[0].left=t[1]
t[0].right=t[2]
t[1].left=t[3]







solution = Solution()
print(solution.rightSideView(t[0]))


