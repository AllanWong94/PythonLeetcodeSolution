class Solution(object):

# Runtime: 166ms Beats or equals to 29%
    def threeSumClosest(self, nums, target):
        nums.sort()
        temp = sum(nums[:3])
        if temp > target:
            return temp
        temp = sum(nums[-3:])
        if temp < target:
            return temp
        res = 10 ** 20
        sumE = 0
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                temp = sum([nums[i], nums[lo], nums[hi]])
                margin = target - temp
                if margin == 0: return target
                if res>abs(margin):
                    res=abs(margin)
                    sumE=temp
                if margin > 0:
                    lo += 1
                else:
                    hi -= 1
        return sumE
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """







solution = Solution()
print(solution.threeSumClosest([0, 2, 1, -3], 1))
