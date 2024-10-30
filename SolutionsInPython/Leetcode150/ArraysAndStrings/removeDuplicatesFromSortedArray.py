# 26. Remove Duplicates from Sorted Array
# Leetcode url - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import List

class Solution(object):
    
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    
    def removeDuplicates(self, nums):
        replace = 1
        for i in range(1, len(nums)):   
            if nums[i-1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace
    
    
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    
    def removeDuplicates1(self, nums: List[int]) -> int:
        k = 0

        elements = set()
        
        for i, num in enumerate(nums):
            if num not in elements:
                elements.add(num)
                nums[k] = nums[i]
                k += 1

        return k