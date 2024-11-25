# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

#  Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0] * len(nums)
        postfixSum = [0] * len(nums)

        for i in range(len(nums)):
            leftSum = prefixSum[i - 1] if i > 0 else 0
            prefixSum[i] = leftSum + nums[i]

        for i in range(len(nums) - 1, -1, -1):
            rightSum = postfixSum[i + 1] if i < len(nums) - 1 else 0
            postfixSum[i] = rightSum + nums[i]

        for i in range(len(nums)):
            if prefixSum[i] == postfixSum[i]:
                return i

        return -1