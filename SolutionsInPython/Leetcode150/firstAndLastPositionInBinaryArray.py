
from typing import List
class Solution:
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