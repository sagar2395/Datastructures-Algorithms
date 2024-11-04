# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            length = r - l
            width = min(height[l], height[r])

            maxArea = max(maxArea, length * width)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return maxArea


