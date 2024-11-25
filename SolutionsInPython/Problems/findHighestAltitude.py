# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

# Example 1:
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Example 2:
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = [0] * (len(gain) + 1)
        maxSum = 0

        for i in range(1, len(prefixSum)):
            prefixSum[i] = prefixSum[i - 1] + gain[i-1]
            if prefixSum[i] > maxSum:
                maxSum = prefixSum[i]

        print(prefixSum)
        return maxSum

        