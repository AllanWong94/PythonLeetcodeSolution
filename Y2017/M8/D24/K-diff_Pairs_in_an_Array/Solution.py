from collections import Counter
class Solution(object):
    # TLEed for [i for i in range(10000)]=>49ms 94%
    def findPairs(self, nums, k):
        if k<0 or not nums or len(nums)==0:
            return 0
        res=0
        if k==0:
            c=Counter(nums)
            freq=c.most_common()
            for num,fre in freq:
                if fre<2:
                    break
                res+=1
            return res
        nums=set(nums)
        for i in nums:
            if i+k in nums:
                res+=1
        return res

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """



# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.findPairs([1,3,1,5,4],0))

