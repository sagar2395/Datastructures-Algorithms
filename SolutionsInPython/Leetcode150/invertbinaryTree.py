# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return

        q = deque([root])

        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if node.left and node.right:
                node.left, node.right = node.right, node.left
            elif node.left is None:
                node.left, node.right = node.right, None
            elif node.right is None:
                node.right, node.left = node.left, None
        return root

        