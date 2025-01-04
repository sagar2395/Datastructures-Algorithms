# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/description/

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if m > 0 and nums[m] < nums[m-1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m 
