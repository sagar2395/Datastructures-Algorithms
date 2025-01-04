# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

from typing import List
class Solution:
    # Approach 1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]

    def binarySearch(self, nums, target, leftBias):    
        l = 0
        r = len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return i
    
    # Approach 2
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findLeft():
            l, r = 0, len(nums) - 1

            while l <= r:
                m = (l + r)//2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    if m > 0 and nums[m] != nums[m - 1]:
                        return m
                    elif m == 0:
                        return m
                    else:
                        r = m - 1

            return - 1

        def findRight():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r)//2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    if m < len(nums) - 1 and nums[m] != nums[m + 1]:
                        return m
                    elif m == len(nums) - 1:
                        return m
                    else:
                        l = m + 1

            return -1

        left = findLeft()
        right = findRight()
        return [left, right]