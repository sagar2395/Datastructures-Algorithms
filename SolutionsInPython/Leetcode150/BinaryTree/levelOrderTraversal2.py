# 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]

# Example 2:\
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([root])
        result = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)

        return result[::-1]

            
                
