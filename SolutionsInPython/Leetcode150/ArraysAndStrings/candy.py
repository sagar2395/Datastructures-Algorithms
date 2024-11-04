# 135. Candy
# https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.


from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                arr[i] = arr[i-1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)

        return sum(arr)
