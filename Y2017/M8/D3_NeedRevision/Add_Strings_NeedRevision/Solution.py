from itertools import zip_longest
class Solution(object):
    #Runtime: 52ms Fastest.
    #Reference: https://discuss.leetcode.com/topic/62344/python-7-line-52ms-1-liner-for-fun
    def addStrings(self, num1, num2):
        z = zip_longest(num1[::-1], num2[::-1], fillvalue='0')
        carry, zero2, res = 0, 2 * ord('0'), []
        for i in z:
            sum = ord(i[0]) + ord(i[1]) - zero2 + carry
            res.append(str(sum % 10))
            carry = sum // 10
        return ('1' if carry else '') + ''.join(res[::-1])
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
