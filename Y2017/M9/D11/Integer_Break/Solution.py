    # Runtime: 49ms Beats or equals to 20%
class Solution(object):
    def integerBreak(self, n):
        if n<4:
            return n-1
        ans=1
        for i in range(2,n//2+1):
            ans=max(ans, self.breakNum(n,i))
        return ans


        """
        :type n: int
        :rtype: int
        """


    def breakNum(self, n, num):
        base=n//num
        num_of_base_plus_1=n-num*base
        num_of_base=num-num_of_base_plus_1
        return (base**num_of_base)*((base+1)**num_of_base_plus_1)






solution = Solution()
print(solution.integerBreak(8))

