class Solution(object):
    # TLEed.
    def lastRemaining(self, n):
        right=True
        res=[i for i in range(1,n+1)]
        while len(res)>1:
            if right:
                for i in range(0,(len(res)+1)//2):
                    res.pop(i)
            else:
                for i in range(len(res)-1,-1,-2):
                    res.pop(i)
            right=not right
        return res[0]





        """
        :type n: int
        :rtype: int
        """




# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.lastRemaining(9))

