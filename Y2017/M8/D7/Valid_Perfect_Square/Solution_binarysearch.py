class Solution(object):
    # Runtime: 25ms Beats or equals to 100%
    def isPerfectSquare(self, num):
        lo, hi = 0, num
        while lo<hi:
            mid=(lo+hi)//2
            temp=mid ** 2
            if temp>num:
                hi=mid
            elif temp<num:
                lo=mid+1
            else:
                return True
        return False
        """
        :type num: int
        :rtype: bool
        """