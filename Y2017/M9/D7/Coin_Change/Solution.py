# Runtime: 966ms Beats or equals to 86%
# Reference: https://discuss.leetcode.com/topic/32589/fast-python-bfs-solution
# BFS solution.

class Solution(object):
    def coinChange(self, coins, amount):
        coins = sorted(coins, reverse=True)
        if amount==0:
            return 0
        if amount<coins[-1]:
            return -1
        check = [0] + [-1] * amount
        ptr = 0
        while ptr < amount + 1:
            if check[ptr] == -1:
                ptr += 1
                continue
            for coin in coins:
                if ptr+coin < amount+1 and (check[ptr+coin]==-1 or check[ptr]+1<check[ptr+coin]):
                    check[ptr+coin]=check[ptr]+1
            ptr+=1
        return check[amount]
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """






# solution = Solution()
# print(solution.coinChange([1], 1))

# Runtime: 840ms
# def coinChange(self, coins, amount):
#     level = seen = {0}
#     number = 0
#     while level:
#         if amount in level:
#             return number
#         level = {a+c for a in level for c in coins if a+c <= amount} - seen
#         seen |= level
#         number += 1
#     return -1

print({1,2,3}-{3})

