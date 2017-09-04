#TLEed for long s.
res=0
class Solution(object):
    def numDecodings(self, s):
        if len(s)==0 or s[0]=='0':
            return 0
        global res
        res = 0
        def helper(index):
            global res
            if index == len(s):
                res += 1
            elif index<len(s):
                if int(s[index]) > 0:
                    helper(index + 1)
                if s[index]!='0' and 0 < int(s[index:index + 2]) < 27:
                    helper(index + 2)
        helper(0)
        return res

    """
    :type s: str
    :rtype: int
    """



# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.numDecodings('123'))

