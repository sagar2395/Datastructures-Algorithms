# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float("inf")
        resultSum = 0

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]

                if curSum == target:
                    return curSum

                if abs(curSum - target) < abs(closestSum - target):
                    closestSum = curSum

                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return closestSum



