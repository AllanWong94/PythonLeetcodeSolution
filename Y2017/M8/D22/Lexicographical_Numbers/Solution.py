class Solution(object):
    #MLEed for input 49999.
    def lexicalOrder(self, n):
        nums=[str(i) for i in range(1,n+1)]
        nums.sort()
        nums=[int(i) for i in nums]
        return nums



        """
        :type n: int
        :rtype: List[int]
        """



# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.lexicalOrder(49999))

