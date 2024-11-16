# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        count = 0
        while q:
            row = []

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    row.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            row = row[::-1] if count % 2 else row
            if row != []:
                res.append(row)
        
            count += 1

        return res