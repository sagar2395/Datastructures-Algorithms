# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left