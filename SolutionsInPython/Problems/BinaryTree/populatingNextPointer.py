# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/?envType=problem-list-v2&envId=linked-list

from collections import deque
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        q = deque([root])
        while q:
            qLen = len(q)
            prev = q.popleft()
            if not prev: 
                break
            q.append(prev.left)
            q.append(prev.right)
            for i in range(qLen - 1):
                curr = q.popleft()
                prev.next = curr
                prev = curr
                q.append(curr.left)
                q.append(curr.right)

        return root
            