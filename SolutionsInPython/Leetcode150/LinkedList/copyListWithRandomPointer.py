# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head

        while cur:
            copy  = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next] 
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]