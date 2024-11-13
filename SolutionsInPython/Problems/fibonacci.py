# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=EASY&status=TO_DO

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3. 

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    
    def fib_recursive(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

    def fib_dp(self, n: int) -> int:

        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]    
    
    