# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur, num):
            if not cur:
                return 0

            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                return num

            
            return dfs(cur.left, num) + dfs(cur.right, num)

        return dfs(root, 0)
    
    # Another approach to solve above problem
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root, curSum):
            if not root:
                return
            
            curSum = (curSum * 10) + root.val
            if not root.left and not root.right:
                nonlocal result
                result += curSum

            dfs(root.left, curSum)
            dfs(root.right, curSum)

        dfs(root, 0)
        return result