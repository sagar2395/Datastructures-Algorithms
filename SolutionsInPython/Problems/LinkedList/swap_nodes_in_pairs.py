# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/?envType=problem-list-v2&envId=linked-list&difficulty=MEDIUM

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Explanation:



# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3]

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # Save pointers
            second = curr.next
            nxtPair = curr.next.next

            # Reverse Operation
            second.next = curr
            prev.next = second
            curr.next = nxtPair

            # Update pointers
            prev = curr
            curr = nxtPair

        return dummy.next