# 997. Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/description/?envType=problem-list-v2&envId=graph&difficulty=EASY&status=TO_DO

# Example 1:
# Input: n = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCnt = [0] * n
        for i in trust:
            trustCnt[i[0] - 1] -= 1
            trustCnt[i[1] - 1] += 1
        for i in range(n):
            if trustCnt[i] == n - 1:
                return i + 1
        
        return -1