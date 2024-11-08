# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/?envType=problem-list-v2&envId=binary-tree&difficulty=EASY

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True 

        def isInverse(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            if left.val != right.val:
                return False
            
            return isInverse(left.left, right.right) and isInverse(left.right, right.left)

        return isInverse(root.left, root.right)