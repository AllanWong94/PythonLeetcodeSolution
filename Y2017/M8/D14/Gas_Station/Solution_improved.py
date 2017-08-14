# Runtime: 39ms Beats or equals to 67%
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(cost)>sum(gas):
            return -1
        gas_left = gas_needed = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_left += g - c
            if gas_left < 0:
                gas_needed -= gas_left
                start = i + 1
                gas_left = 0
        return start






