# 27. Remove Element
# Leetcode URL - https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import List
class Solution:
    
    ## My appraoch (Not efficient)
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        for i, num in enumerate(nums):
            if num == val:
                count += 1
                nums[i] = float("inf")

        nums.sort()
        print(nums)
        return len(nums) - count
    
    def removeElement1(self, nums: List[int], val: int) -> int:
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k

sol = Solution()
sol.removeElement([0,1,2,2,3,0,4,2], 2)
