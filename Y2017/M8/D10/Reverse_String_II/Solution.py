class Solution(object):
# Runtime: 45ms=>32ms Beats or equals to 46%=>96%
    def reverseStr(self, s, k):
        start,length=0,len(s)
        res = ''
        while length > start:
            res+=s[start:k+start][::-1]
            res+=s[k+start:2*k+start]
            start += 2*k
        return res

        """
        :type s: str
        :type k: int
        :rtype: str
        """







solution = Solution()
print(solution.reverseStr('abcdefg', 2))
