# Runtime: 112ms Beats or equals to 29%
class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        A=sum(nums)-sum([i for i in range(1,n+1)])
        B=sum([i*i for i in nums])-sum([i*i for i in range(1,n+1)])
        return [(A+B/A)//2,(B/A-A)//2]


        # Runtime:56ms
        # Calculate it instead of dumb aggregations!
        # def findErrorNums(self, nums):
        #     """
        #     :type nums: List[int]
        #     :rtype: List[int]
        #     """
        #     N = len(nums)
        #     alpha = sum(nums) - N * (N + 1) / 2
        #     beta = (sum(x * x for x in nums) - N * (N + 1) * (2 * N + 1) / 6) / alpha
        #     return (alpha + beta) / 2, (beta - alpha) / 2
        # """
        # :type nums: List[int]
        # :rtype: List[int]
        # """





solution = Solution()
print(solution.findErrorNums([1,2,2,4]))

