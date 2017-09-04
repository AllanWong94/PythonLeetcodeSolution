# Runtime: 36ms
import sys
class Solution(object):
    def increasingTriplet(self, nums):
        c1=c2=sys.maxint
        for i in nums:
            if i<=c1:
                c1=i
            elif i<=c2:
                c2=i
            else:
                return True
        return False


        """
        :type nums: List[int]
        :rtype: bool
        """








solution = Solution()
print(solution.increasingTriplet([5,1,5,5,2,5,4]))

