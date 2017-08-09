class Solution(object):
    #TLEed.
    def findRadius(self, houses, heaters):
        radius=[]
        for house in houses:
            temp=1000000
            for heater in heaters:
                temp=min(temp, abs(heater-house))
            radius.append(temp)
        return max(radius)
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
