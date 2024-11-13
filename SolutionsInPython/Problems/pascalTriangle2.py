# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=EASY&status=TO_DO

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            temp = [0] + res + [0]
            tempResult = []
            for j in range(i + 2):
                tempResult.append(temp[j] + temp[j + 1])
            res = tempResult

        return res
