# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode

#TLEed.

class Solution(object):
    def isSubtree(self, s, t):
        return self.helper(s,t,False,t)

    def helper(self,s,t,root_found,origin_t):
        if root_found:
            if s and s.val==origin_t.val:
                if self.helper(s.left,origin_t.left, True, origin_t) and self.helper(s.right,origin_t.right, True, origin_t):
                    return True
            if (not s and t) or (s and not t):
                return False
            if (not s and not t):
                return True
            return self.helper(s.left,t.left, True, origin_t) and self.helper(s.right,t.right, True, origin_t)
        else:
            if not s or not t:
                return False
            if s.val==t.val:
                return self.helper(s.left, t.left, True, origin_t) and self.helper(s.right, t.right, True, origin_t)
            return self.helper(s.left, t, False, origin_t) or self.helper(s.right, t, False, origin_t)



        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """



# Runtime: ms Beats or equals to %


t1=TreeNode(1)
t2=TreeNode(1)
t3=TreeNode(1)
t1.left=t2


solution = Solution()
print(solution.isSubtree(t1,t3))


