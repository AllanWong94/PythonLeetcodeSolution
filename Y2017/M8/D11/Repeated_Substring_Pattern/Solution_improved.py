# Runtime: 65ms Beats or equals to 58%
class Solution(object):
    def repeatedSubstringPattern(self, s):
        length=len(s)
        for i in range(1, length // 2+1):
            if (length%i==0) and (s[0]==s[i]):
                start=i
                sample=s[:i]
                while start<length:
                    if sample!=s[start:start+i]:
                        break
                    start+=i
                else:
                    return True
        return False

        """
        :type s: str
        :rtype: bool
        """








solution = Solution()
print(solution.repeatedSubstringPattern("abac"))

