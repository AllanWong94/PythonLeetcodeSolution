# Reference: https://discuss.leetcode.com/topic/35253/explanation-of-super-easy-java-solution-beats-98-8-from-pinkfloyda/7
class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        st,ed=sorted([i.start for i in intervals]),sorted([i.end for i in intervals])
        end=0
        for i in range(len(intervals)):
            if st[i]>=ed[end]:
                end+=1
        return len(intervals)-end
