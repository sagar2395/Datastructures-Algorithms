# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

from typing import List, Optional
from Tree import Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    
    def buildTree(self, inorder: List[int], postorder: List[int], count: int) -> Optional[TreeNode]:
        print("-----Start: " + str(count) +"------------")
        print("Inorder: "+ str(inorder))
        print("Postorder: " + str(postorder))
        print("buildTree({inorder})")
        tree = Tree()
        
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        print("Creating root: " + str(root.val))
        
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx+1:], postorder, count + 1)
        root.left = self.buildTree(inorder[:idx], postorder, count + 1)
        tree.PrintTree(root)
        print("-----End: " + str(count) +"------------")
        return root

a = Solution()
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

root = a.buildTree(inorder, postorder, 0)

# tree = Tree()
# print(tree.inorderTraversal(root))
# print(tree.PrintTree(root))

