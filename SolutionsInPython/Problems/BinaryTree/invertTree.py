# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/?envType=problem-list-v2&envId=binary-tree&difficulty=EASY

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inverseChildren(root):

            if not root:
                return
            root.left, root.right = root.right, root.left
            inverseChildren(root.left)
            inverseChildren(root.right)

        inverseChildren(root)
        return root