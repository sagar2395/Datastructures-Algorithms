# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

# Example 2:
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

# Example 3:
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]

        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax