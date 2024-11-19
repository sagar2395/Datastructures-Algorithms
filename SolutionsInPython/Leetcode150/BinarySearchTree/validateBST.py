# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, minimum, maximum):
            if not node:
                return True

            if not (node.val > minimum and node.val < maximum):
                return False

            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        return valid(root, float("-inf"), float("inf"))

        return isLeftValid and isRightValid