class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        numHouse, numHeater = len(houses), len(heaters)
        if numHouse == 0:
            return 0
        curHouse, curHeater = 0, 0
        houses.sort()
        heaters.sort()
        # print houses
        # print heaters
        minR = 0
        while curHouse < numHouse:
            dist1 = abs(houses[curHouse]-heaters[curHeater])
            if dist1 > minR:
                while curHeater + 1 < numHeater:
                    dist2 = abs(houses[curHouse]-heaters[curHeater+1])
                    if dist2 <= minR:
                        curHeater += 1
                        break
                    elif dist1 < dist2:
                        minR = dist1
                        break
                    else:
                        dist1 = dist2
                        curHeater += 1
                else:
                    minR = dist1
            curHouse += 1
        return minR