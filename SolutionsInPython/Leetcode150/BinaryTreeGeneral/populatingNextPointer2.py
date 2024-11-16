# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=problem-list-v2&envId=linked-list

# Example 1:
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:
# Input: root = []
# Output: []

from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque([root])

        while q:
            qLen = len(q)
            prev = None
            for i in range(qLen):
                curr = q.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr and curr.left:
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)

        return root