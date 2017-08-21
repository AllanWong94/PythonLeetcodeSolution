# Runtime: 442ms Beats or equals to 32%
# Reference: https://discuss.leetcode.com/topic/88520/python-straightforward-with-explanation-o-st-and-o-s-t-approaches

class Solution(object):
    def isMatch(self, s, t):
        if not (s and t):
            return s is t
        return s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)

    def isSubtree(self, s, t):
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
