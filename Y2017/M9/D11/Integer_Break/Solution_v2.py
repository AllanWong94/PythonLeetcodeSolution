# Runtime: 26ms
# Reference: https://leetcode.com/submissions/detail/118466079/
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        else:
            out = 4
            for i in range(5, n + 1):
                if out % 2 == 0:
                    out = (out / 2) * 3
                else:
                    out = (out / 3) * 4
            return out
