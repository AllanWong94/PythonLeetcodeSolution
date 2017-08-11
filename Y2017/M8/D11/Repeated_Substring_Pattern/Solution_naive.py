# Runtime: 232ms Beats or equals to 23%
class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(1, len(s) // 2+1):
            sample = s[:i]
            if not len(s) % len(sample):
                if self.determine(s,sample):
                    return True
        return False

    def determine(self, s, sample):
        length = len(sample)
        start, end = length, 2 * length
        while start < len(s):
            if s[start:end] != sample:
                return False
            start,end=end,end+length
        return True
        """
        :type s: str
        :rtype: bool
        """








solution = Solution()
print(solution.repeatedSubstringPattern("abac"))

