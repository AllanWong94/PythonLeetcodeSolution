class Solution(object):
    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer
        """
        :type nums: List[int]
        :rtype: int
        """


# Runtime: ms Beats or equals to %





solution = Solution()

nums=[3,10,5,25,2,8]
print(solution.findMaximumXOR(nums))


for i in nums:
    print(bin(i))