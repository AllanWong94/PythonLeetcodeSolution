class Solution(object):
    # Runtime: 30ms fastest
    # Reference: https://discuss.leetcode.com/topic/85029/python-simple-explanation
    def findLUSlength(self, A, B):
        if A == B:
            return -1
        return max(len(A), len(B))
        """
        :type a: str
        :type b: str
        :rtype: int
        """
