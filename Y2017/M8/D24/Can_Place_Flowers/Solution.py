# Runtime: 62ms Beats or equals to 68%

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed.insert(0,0)
        flowerbed.append(0)
        count=0
        index=0
        while n>0:
            if index==len(flowerbed):
                if count>0:
                    n -= (count - 1) // 2
                    return n<=0
                else:
                    return False
            if flowerbed[index]:
                if count>0:
                    n-=(count-1)//2
                count=0
            else:
                count+=1
            index+=1
        return True



        # Runtime:59ms
        # skipped unnecessary slots.
        # def canPlaceFlowers(self, flowerbed, n):
        #     """
        #     :type flowerbed: List[int]
        #     :type n: int
        #     :rtype: bool
        #     """
        #     if n == 0:
        #         return True
        #     i, length = 0, len(flowerbed)
        #     flowerbed.append(0)  # 如果最后的数字就已经为0了，那么什么也不做
        #     while i < length and n != 0:
        #         if flowerbed[i] == 1:
        #             i = i + 2
        #         elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:  # flowerbed[i]==0
        #             flowerbed[i] = 1
        #             i, n = i + 2, n - 1
        #         else:
        #             i = i + 1
        #     if n == 0:
        #         return True
        #     return False


        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """








solution = Solution()
print(solution.canPlaceFlowers([0,0,1,0,1],1))

