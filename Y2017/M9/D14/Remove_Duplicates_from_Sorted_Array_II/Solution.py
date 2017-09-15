# Runtime: 78ms Beats or equals to 15%
from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count=sorted(Counter(nums).most_common(),key=lambda x:x[0])
        ptr=0
        for num,c in count:
            for i in range(min(c,2)):
                nums[ptr]=num
                ptr+=1
        return ptr



        """
        :type nums: List[int]
        :rtype: int
        """






solution = Solution()
print(solution.removeDuplicates([1]))

