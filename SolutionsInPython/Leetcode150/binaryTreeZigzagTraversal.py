# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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