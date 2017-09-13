class Solution(object):
    # dp[n][0]=>action: buy
    # dp[n][1]=>action: sell
    # dp[n][2]=>action: nothing
    def maxProfit(self, prices):
        dp=[[0]*len(prices) for i in range(3)]
        dp[1]=max(prices[1]-prices[0],0)
        for i in range(2,len(prices)):
            dp[i][0]=dp[i-2][2]
            dp[i][1]
        # Reference: https://discuss.leetcode.com/topic/33836/4-line-python-solution-52-ms/2
        # def maxProfit(self, prices):
        #     notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        #     for p in prices:
        #         hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        #     return max(notHold, notHold_cooldown)

        """
        :type prices: List[int]
        :rtype: int
        """
