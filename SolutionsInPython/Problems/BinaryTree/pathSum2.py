# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: []

# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: []

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(root, path, pathSum):
            if not root:
                return
            path.append(root.val)
            pathSum += root.val
            if not root.left and not root.right:
                if pathSum == targetSum:
                    result.append(path)
                return              
            
            dfs(root.left, path.copy(), pathSum)
            dfs(root.right, path.copy(), pathSum)


        dfs(root, [], 0)
        return result