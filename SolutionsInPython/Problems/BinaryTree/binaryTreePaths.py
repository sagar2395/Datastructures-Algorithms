# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/?envType=problem-list-v2&envId=binary-tree&difficulty=EASY

# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        s = ""
        def dfs(root, s):
            if not root:
                return
            if not root.left and not root.right:
                result.append(s + str(root.val))
                return
            else:
                s += str(root.val) + "->"
            dfs(root.left, s)
            dfs(root.right,s)
            
        dfs(root, "")
        return result