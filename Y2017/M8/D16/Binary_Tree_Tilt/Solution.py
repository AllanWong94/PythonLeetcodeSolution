# Runtime: 92ms Beats or equals to 58% One-time AC.


from Y2017.TreeNode import TreeNode

class Solution(object):
    tiltSum=0
    def findTilt(self, root):
        self.helper(root)
        return self.tiltSum



    def helper(self,node):
        if not node:
            return 0
        left=self.helper(node.left)
        right=self.helper(node.right)
        self.tiltSum+=abs(left-right)
        return left+right+node.val

        # Runtime: 72ms Fastest.
        # Global value is slow! Try not to use it!
        # def findTilt(self, root):
        #     """
        #     :type root: TreeNode
        #     :rtype: int
        #     """
        #
        #     def dfs(node):
        #         # returns (cum val, cum tilt)
        #         if node:
        #             lw, lt = dfs(node.left)
        #             rw, rt = dfs(node.right)
        #             return node.val + lw + rw, abs(lw - rw) + lt + rt
        #         return 0, 0
        #
        #     return dfs(root)[1]
        """
        :type root: TreeNode
        :rtype: int
        """
