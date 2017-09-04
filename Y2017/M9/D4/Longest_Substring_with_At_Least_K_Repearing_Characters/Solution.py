# Reference: https://discuss.leetcode.com/topic/57092/4-lines-python
class Solution(object):
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c)<k:
                return max(self.longestSubstring(t,k) for t in s.split(c))
        return len(s)

        """
        :type s: str
        :type k: int
        :rtype: int
        """
