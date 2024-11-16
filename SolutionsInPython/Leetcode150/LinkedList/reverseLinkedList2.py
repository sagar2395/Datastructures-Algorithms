# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

from typing import Optional
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        prev = None
        for i in range(right-left+1):
            tempNext = cur.next
            cur.next = prev
            prev, cur = cur, tempNext

        leftPrev.next.next = cur
        leftPrev.next = prev
        return dummy.next
        