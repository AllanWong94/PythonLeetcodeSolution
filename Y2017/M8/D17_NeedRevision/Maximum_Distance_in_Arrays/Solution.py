# Runtime: 56ms Beats or equals to 97%
class Solution(object):
    def maxDistance(self, arrays):
        maxE=[i[-1] for i in arrays]
        minE=[i[0] for i in arrays]
        tempMax,tempMin=max(maxE),min(minE)
        if maxE.index(tempMax)!=minE.index(tempMin):
            return tempMax-tempMin
        maxE.remove(tempMax)
        minE.remove(tempMin)
        return max(max(maxE)-tempMin,tempMax-min(minE))

        """
        :type arrays: List[List[int]]
        :rtype: int
        """









solution = Solution()
print(solution.maxDistance([[1],[2]]))

