# Runtime: 35ms Beats or equals to 60% One-time AC. Fastest.
class Solution(object):
    def countSegments(self, s):
        return len([i for i in s.split(' ') if i !=''])

        """
        :type s: str
        :rtype: int
        """
