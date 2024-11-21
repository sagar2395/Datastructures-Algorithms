# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# Example 2:
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def func(i,buy,prices,ct,dic):
            if i>=len(prices) or ct==0:
                return 0
            
            if (i,buy,ct) in dic:
                return dic[(i,buy,ct)]
            
            x,y,a,b=0,0,0,0
            
            if buy:
                x=-prices[i]+func(i+1,False,prices,ct,dic)
                y=0+func(i+1,buy,prices,ct,dic)
            else:
                a=prices[i]+func(i+1,True,prices,ct-1,dic)
                b=0+func(i+1,buy,prices,ct,dic)
            dic[(i,buy,ct)]=max(a,b,x,y)
            return max(a,b,x,y)
        
        return func(0,True,prices,k,{})