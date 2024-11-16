# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 6

# Example 2:
# Input: root = []
# Output: 0

# Example 3:
# Input: root = [1]
# Output: 1

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, sum):
            if not node:
                return 0

            if not node.left and not node.right:
                return 1

            sum += dfs(node.left, sum) + dfs(node.right, sum)
            return sum
        return dfs(root, 1)