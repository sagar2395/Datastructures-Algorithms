# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, sum):
            if not node:
                return 0

            if not node.left and not node.right:
                return 1

            sum += dfs(node.left, sum) + dfs(node.right, sum)
            return sum
        return dfs(root, 1)