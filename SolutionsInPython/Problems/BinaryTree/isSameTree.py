# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/?envType=problem-list-v2&envId=binary-tree&difficulty=EASY

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false 

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def nodeComparison(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return nodeComparison(p.left, q.left) and nodeComparison(p.right, q.right)

        return nodeComparison(p, q)