# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepthBFS(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
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
               
        