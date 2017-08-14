# Runtime: 32ms=>28ms Beats or equals to 89%=>fastest
class Solution(object):
    def isStrobogrammatic(self, num):
        if len(num) == 0:
            return False
        nums = {'9': '6', '6': '9', '0': '0', '1': '1', '8': '8'}
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if num[lo] not in nums or nums[num[lo]] != num[hi]:
                return False
            lo += 1
            hi -= 1
        return True
        """
        :type num: str
        :rtype: bool
        """

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'6': '9', '9': '6', '0': '0', '1': '1', '8': '8'}
        end = len(num) / 2
        if len(num) % 2 == 1:
            end += 1
        for i in range(int(end)):
            if num[i] not in dic or dic[num[i]] != num[len(num) - 1 - i]:
                return False

        return True


solution = Solution()
print(solution.isStrobogrammatic('191'))
