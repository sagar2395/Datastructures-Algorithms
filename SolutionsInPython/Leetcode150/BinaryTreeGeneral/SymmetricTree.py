# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

from typing import Optional
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and self.dfs(left.left, right.right) and self.dfs(left.right, right.left))
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSame(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False

            return isSame(l.left, r.right) and isSame(l.right, r.left) and l.val == r.val

        return isSame(root.left, root.right)