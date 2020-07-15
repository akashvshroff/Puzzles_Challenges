class Solution(object):
    def maxProfit(self, prices):
        """
        Find out the maximum profit from buying and selling shares with only
        one transaction at a time.
        See also: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
