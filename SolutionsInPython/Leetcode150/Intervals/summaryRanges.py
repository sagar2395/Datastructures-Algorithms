# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

from typing import List
class Solution(object):
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            temp = i
            while temp < len(nums) - 1 and nums[temp+1] - nums[temp] == 1:
                temp += 1
                
            if(nums[temp] == nums[i]):
                res.append(str(nums[temp]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[temp]))
                
            i = temp + 1
            
        return res
                
                
range = Solution()
print(range.summaryRanges([0,1,2,4,5,7]))