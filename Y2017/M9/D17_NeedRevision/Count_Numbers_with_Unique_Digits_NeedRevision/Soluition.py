# Runtime: 29ms Beats or equals to 94%

choices=[9,9,8,7,6,5,4,3,2,1]
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        choices=[9,9,8,7,6,5,4,3,2,1]
        ans=product=1
        for i in range(min(10,n)):
            product*=choices[i]
            ans+=product
        return ans
        """
        :type n: int
        :rtype: int
        """









solution = Solution()
print(solution.countNumbersWithUniqueDigits(3))