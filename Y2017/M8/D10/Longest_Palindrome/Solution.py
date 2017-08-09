class Solution(object):
    def longestPalindrome(self, s):

    #Runtime: 42ms Beats or equals to 82%
        store=[False]*123
        res=0
        for c in s:
            store[ord(c)]=not store[ord(c)]
            if not store[ord(c)]:
                res+=2
        if res<len(s): res+=1
        return res

        """
        :type s: str
        :rtype: int
        """






solution = Solution()
print(solution)

