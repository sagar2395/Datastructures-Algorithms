# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There are two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # DFS approach
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum

            return (dfs(node.left, curSum) or dfs(node.right, curSum))

        return dfs(root, 0)
    
    # Backtracking approach
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        pathSum = 0

        def backtrack(head):

            if not head:
                return False
            
            nonlocal pathSum
            pathSum += head.val

            if not head.left and not head.right and pathSum == targetSum:
                return True
            
            if backtrack(head.left):
                return True
            if backtrack(head.right):
                return True

            pathSum -= head.val

            return False

        return backtrack(root)
    
    # BFS approach
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False

        q = deque()
        q.append((root, 0))

        while q:
            current, s = q.popleft() 
            if current.left:
                q.append((current.left, s + current.val))
            if current.right:
                q.append((current.right, s + current.val))
            if s + current.val == targetSum and not current.left and not current.right:
                return True

        return False