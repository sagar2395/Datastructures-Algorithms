# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/?envType=problem-list-v2&envId=two-pointers&status=TO_DO&difficulty=EASY

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                count += 1
            else:
                nums[i] = nums[j]
                i += 1
            j += 1

        for k in range(i, len(nums)):
            nums[k] = 0 
        