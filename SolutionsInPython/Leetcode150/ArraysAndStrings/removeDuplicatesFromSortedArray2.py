# 80. Remove Duplicates from Sorted Array II
# Leetcode URL - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            count = 1 
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            r += 1
        return l 
    
    def removeDuplicates1(self, nums: List[int]) -> int:
        k = 0
        elements = {}

        for i, num in enumerate(nums):
            if num not in elements:
                elements[num] = 1
                nums[k] = num
                k += 1
            elif elements[num] < 2:
                elements[num] += 1
                nums[k] = num
                k += 1
        
        return k