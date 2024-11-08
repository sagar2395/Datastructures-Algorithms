# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=MEDIUM

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        numNodes = 0

        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            curr = curr.next
            numNodes += 1

        nthNode = numNodes - n + 1

        curr = dummy
        for i in range(nthNode - 1):
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

        return dummy.next

            