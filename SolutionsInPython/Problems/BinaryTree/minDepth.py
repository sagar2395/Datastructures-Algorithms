# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/?envType=problem-list-v2&envId=binary-tree&difficulty=EASY

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left    
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0

            if not root.left:
                return 1 + dfs(root.right)

            if not root.right:
                return 1 + dfs(root.left)

            return 1 + min(dfs(root.left), dfs(root.right))
         
        return dfs(root)