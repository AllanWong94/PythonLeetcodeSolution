class Solution(object):
    # Runtime: 52ms Beats or equals to 99.2%
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        res = sum(nums[:3])
        if length == 3:
            return res
        for i in range(length - 2):
            lo, hi = i + 1, length - 1
            if i < length - 3 and (sum(nums[i:i + 3]) > target):
                return res
            if i < hi - 1 and sum([nums[i], nums[hi - 1], nums[hi]]) < target:
                res = sum([nums[i], nums[hi - 1], nums[hi]])
                continue
                # lo=hi
                # res=sum([nums[i],nums[hi-1],nums[hi]])
            while lo < hi:
                temp = sum([nums[i], nums[lo], nums[hi]])
                if temp == target: return target
                if temp < target:
                    lo += 1
                else:
                    hi -= 1
                if abs(res - target) > abs(temp - target):
                    res = temp
        return res
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


solution = Solution()
nums = [0, 2, 1, -3]
i = 1
print(sum(nums[i:i + 3]))
print(solution.threeSumClosest([0, 2, 1, -3], 1))
