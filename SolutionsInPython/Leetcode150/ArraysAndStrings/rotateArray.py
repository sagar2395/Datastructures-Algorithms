

from typing import List

class Solution:
    
    # This solution rotates elements one by one. Not efficient.
    # Time Complexity - O(n2)
    # Space complexity - O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums[-1]
            for num in range(len(nums) - 2, -1, -1):
                 nums[num + 1] = nums[num]
            nums[0] = temp


    # More efficient method without extra space
    # Time complexity - O(n)
    # Space complexity - O(1)
    
    # Solution Summary - We are reversing whole array at once first and then reversing array from 0 to k and k + 1 to last element.
    
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
         
        