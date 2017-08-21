# Runtime: 52ms Beats or equals to 86%
# O(1) space requirement not met

class Solution(object):
    def nextPermutation(self, nums):
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                temp=nums[i-1]+1
                while temp not in nums[i:]:
                    temp+=1
                nums[i-1],temp=temp,nums[i-1]
                store=nums[i:]
                store.remove(nums[i-1])
                store.append(temp)
                store.sort()
                for k in range(len(nums)-i):
                    nums[i+k]=store[k]
                return
        nums.sort()
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
