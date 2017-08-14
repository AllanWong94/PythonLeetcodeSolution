# Runtime: 39ms Beats or equals to 67%
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(cost)>sum(gas):
            return -1
        cur=start = 0
        for i in range(len(gas)):
            cur+=gas[i]-cost[i]
            if cur<0:
                start=i+1
                cur=0
        return start






