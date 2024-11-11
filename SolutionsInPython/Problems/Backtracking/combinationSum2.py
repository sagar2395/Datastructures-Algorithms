# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/?envType=problem-list-v2&envId=backtracking

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        print("Input: " + str(candidates) + ", target: " + str(target))

        def backtrack(path, start, total):
            print("backtrack("+str(path)+", "+str(start)+", "+str(total)+")")
            if total == target:
                print("found result. Appending to path: "+str(path))
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(path, i + 1, total + candidates[i])
                print("Popping last element of path: " + str(path[-1]))
                path.pop()

        backtrack([], 0, 0)
        return result
    
a = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print("Input: " + str(candidates) + ", target: " + str(target))
result = a.combinationSum2([10,1,2,7,6,1,5], 8)
print(result)