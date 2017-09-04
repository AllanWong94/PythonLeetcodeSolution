# Runtime: 39ms Beats or equals to 55%
class Solution(object):
    def increasingTriplet(self, nums):
        val1=[]
        val2=None
        for i in nums:
            if not val1 or i>val1[-1]:
                val1.append(i)
                if len(val1)==3:
                    return True
            elif val1:
                if len(val1)==1:
                    val1[0]=i
                else:
                    if val1[0]<i<val1[1]:
                        val1[1]=i
                    else:
                        if not val2 or val2>i:
                            val2=i
                        else:
                            val1=[val2,i]
                            val2=None
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """








solution = Solution()
print(solution.increasingTriplet([5,1,5,5,2,5,4]))

