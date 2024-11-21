# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


from typing import List
from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dp(idx,state,trans):
            if idx >= len(prices):
                return 0
            if trans >= 2:
                return 0

            if (idx,state,trans) not in memo:
                if not state:   #buy
                    memo[(idx,state,trans)] = max(dp(idx+1, not state,trans) - prices[idx] , dp(idx+1,state,trans))
                else:   #sell
                    memo[(idx,state,trans)] = max(dp(idx+1, not state,trans+1) + prices[idx], dp(idx+1,state,trans))   
            return memo[(idx,state,trans)]
            
        return dp(0,False,0)