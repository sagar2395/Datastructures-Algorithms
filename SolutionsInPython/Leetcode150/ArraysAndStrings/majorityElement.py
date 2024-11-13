

# 169. Majority Element
# Leetcode Url - https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List
 
class Solution:
    
    ## This solution is unoptimized using dictionary to store quantity of each element
    ## Time complexity - O(n)
    ## Space complexity - O(n)
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        maxQuantity = 0 
        maxNum = -1

        for num in nums:
            if num not in dict:
                dict[num] = 1
                if dict[num] > maxQuantity:
                    maxNum = num
                    maxQuantity = dict[num]

            else:
                dict[num] += 1
                if dict[num] > maxQuantity:
                    maxNum = num
                    maxQuantity = dict[num]

        return maxNum
    
    # Same complexity as above but this solution is more concise
    
    def majorityElement1(self, nums: List[int]) -> int:
            hash = {}
            res = majority = 0

            for n in nums:
                hash[n] = 1 + hash.get(n, 0)
                if hash[n] > majority:
                    res = n
                    majority = hash[n]

            return res
        
    def majorityElement2(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n

            count += 1 if n == res else  -1

        return res