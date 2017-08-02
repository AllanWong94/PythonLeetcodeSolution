# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    # Runtime: 42ms Beats or equals to 22%
    # Reference: https://discuss.leetcode.com/topic/8474/9-line-61ms-ac-python-solution-with-comments
    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""] * 4
            cur = min(read4(buf4), n - idx)
            for i in range(cur):
                buf[idx] = buf4[i]
                idx += 1
            if cur != 4 or idx == n:
                return idx

        # Runtime: 29ms
        # def read(self, buf, n):
        #     """
        #     :type buf: Destination buffer (List[str])
        #     :type n: Maximum number of characters to read (int)
        #     :rtype: The number of characters read (int)
        #     """
        #     ptr = 0
        #     while ptr < n:
        #         tmpBuf = [''] * 4
        #         cnt = read4(tmpBuf)
        #         if not cnt:
        #             return ptr
        #         if ptr + cnt < n:
        #             buf[ptr:ptr + cnt] = tmpBuf
        #             ptr += cnt
        #         else:
        #             for i in range(ptr, n):
        #                 buf[i] = tmpBuf[i - ptr]
        #             ptr = n
        #
        #     return ptr

        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """




solution = Solution()
print(solution)