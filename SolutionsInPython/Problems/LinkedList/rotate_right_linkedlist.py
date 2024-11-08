# 61. Rotate List
# https://leetcode.com/problems/rotate-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=MEDIUM

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        if not head:
            return None

        totalNodes = 0
        while curr.next:
            curr = curr.next
            totalNodes += 1

        k = k % totalNodes

        if k == 0:
            return head

        nthNode = totalNodes - k

        prev = dummy

        for i in range(nthNode):
            prev = prev.next

        curr.next = dummy.next 
        dummy.next = prev.next
        prev.next = None
        

        return dummy.next

