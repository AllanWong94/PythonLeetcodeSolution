class Solution(object):
    # Runtime: 45ms=>32ms Beats or equals to 45%=>91%
    def thirdMax(self, nums):
        a=b=c=None
        for i in nums:
            if i>a:
                a,b,c=i,a,b
            elif a>i>b:
                b,c=i,b
            elif b>i>c:
                c=i
        return c if not c is None else a
        """
        :type nums: List[int]
        :rtype: int
        """



solution = Solution()
print(solution.thirdMax([1,2]))

