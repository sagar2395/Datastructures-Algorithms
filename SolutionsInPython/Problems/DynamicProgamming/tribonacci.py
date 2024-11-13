# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=EASY&status=TO_DO

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:s
# Input: n = 25
# Output: 1389537

class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = [0] * (n + 3)
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]  

        return dp[n]
    
    # Slower approach. it is not passing all the test cases in leetcode
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)