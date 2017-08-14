class Solution(object):
    # TLEed.
    def canCompleteCircuit(self, gas, cost):
        if sum(cost)>sum(gas):
            return -1
        length=len(gas)
        while i<length:
            tank=0
            for j in range(length):
                stop=(i+j)%length
                tank+=gas[stop]-cost[stop]
                if tank<0:
                    i=stop+1
                    break
            else:
                return i


        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """



# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.canCompleteCircuit([2,3,1],[3,1,2]))

