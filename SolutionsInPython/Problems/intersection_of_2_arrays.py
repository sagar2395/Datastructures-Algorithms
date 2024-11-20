# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=two-pointers&status=TO_DO&difficulty=EASY

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = set()

        for num in nums1:
            if num in nums2:
                result.add(num)
        for num in nums2:
            if num in nums1:
                result.add(num)

        return list(result)