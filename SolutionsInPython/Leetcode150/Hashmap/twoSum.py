# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = j = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j):
                    if(target == nums[i] + nums[j]):
                        return [i, j]
                    
    def twoSumsHashmap(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if(diff in dict):
                return i, dict[diff]
            else:
                dict[nums[i]] = i
    