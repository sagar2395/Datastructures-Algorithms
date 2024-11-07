# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        k = 1

        while curr.next:
            curr = curr.next
            k += 1

        curr = head
        elements = deque()

        num = 1
        while num <= k // 2:
            elements.append(curr.val)
            curr = curr.next
            num += 1

        if k % 2 != 0:
            curr = curr.next

        while curr:
            if curr.val != elements.pop():
                return False
            curr = curr.next

        return True

        
