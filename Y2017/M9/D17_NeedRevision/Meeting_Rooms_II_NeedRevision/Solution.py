# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

#TLEed.
class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        minS,maxE=min([k.start for k in intervals]),max([k.end for k in intervals])
        check=[0]*((maxE-minS+1)*2-1)
        for i in intervals:
            for l in range((i.start - minS) * 2, (i.end - minS ) * 2 -1):
                check[l]+=1
        return max(check)

        """
        :type intervals: List[Interval]
        :rtype: int
        """



# Runtime: ms Beats or equals to %




intervals=[Interval(13,15),Interval(1,13)]
solution = Solution()
print(solution.minMeetingRooms(intervals))

