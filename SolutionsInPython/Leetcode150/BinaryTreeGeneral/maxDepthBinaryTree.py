# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        return level
    
    def maxDepthRecursive(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right))
    
    def maxDepthDFS(self, root):        
        stack = [[root, 1]]
        res = 1
        
        while stack:
            node, depth = stack.pop()
            
            if node:
               res = max(res, depth)
               stack.append([node.left, depth + 1]) 
               stack.append([node.right, depth + 1])
               
        return res
               
        