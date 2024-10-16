def buy_sell_stock(nums):
    i = 0
    j = 1
    stocks_difference = 0 
    
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums) - 1):
            temp = nums[j] - nums[i]
        
            if temp > stocks_difference:
                stocks_difference =  temp

    return stocks_difference           

def max_profit_optimised(prices):
    l, r = 0, 1
    maxProfit = 0
    
    while r != len(prices):
        if prices[l] < prices[r]:
            prof = prices[r] - prices[l]
            maxProfit = max(maxProfit, prof)
        else:
            l = r
            
        r += 1
        
    return maxProfit
    

nums = [7,1,5,3,6,4]
print(buy_sell_stock(nums))