# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=problem-list-v2&envId=binary-tree

# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=problem-list-v2&envId=binary-tree&difficulty=EASY



from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Example 1:
    # Input: root = [1,null,2,3]
    # Output: [1,3,2]
    
    # Example 2:
    # Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    # Output: [4,2,6,5,7,1,3,9,8]
    
    # Example 3:
    # Input: root = []
    # Output: []
    
    # Example 4:
    # Input: root = [1]
    # Output: [1]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(root: Optional[TreeNode]):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return result
    
    # Example 1:
    # Input: root = [1,null,2,3]
    # Output: [3,2,1]
    
    # Example 2:
    # Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    # Output: [4,6,7,5,2,9,8,3,1]
    
    # Example 3:
    # Input: root = []
    # Output: []
    
    # Example 4:
    # Input: root = [1]
    # Output: [1]
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
        
        dfs(root)
        return result