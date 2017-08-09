class Solution(object):
    # Runtime: 169ms Beats or equals to 51%
    # Reference: https://discuss.leetcode.com/topic/71456/short-python
    def findRadius(self, houses, heaters):
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i + 2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r