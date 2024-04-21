# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


# Time Complexity: O(n) - beats 45.53% of submissions in Python3
# Space Complexity: O(1) - beats 99.34% of submissions in Python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, max_profit = prices[0], 0
        
        for price in prices[1:]:
            buy_price = min(buy_price, price)
            max_profit = max(max_profit, price - buy_price)

        return max_profit