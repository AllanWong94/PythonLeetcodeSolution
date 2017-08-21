# Runtime: 52ms Beats or equals to 86%
# O(1) space requirement met

class Solution(object):
    def nextPermutation(self, nums):
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                temp=nums[i-1]+1
                while temp not in nums[i:]:
                    temp+=1
                nums[i-1],temp=temp,nums[i-1]
                lo,hi=i,len(nums)-1
                while lo<hi:
                    nums[lo],nums[hi]=nums[hi],nums[lo]
                    lo+=1
                    hi-=1
                for k in range(i,len(nums)):
                    if nums[k]==nums[i-1]:
                        nums[k]=temp
                        return
                return
        nums.sort()
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """





solution = Solution()
print(solution.nextPermutation([2,3,1,3,3]))

