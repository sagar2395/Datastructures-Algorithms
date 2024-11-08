# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=problem-list-v2&envId=linked-list&difficulty=MEDIUM

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:
# Input: head = [1,1,1,2,3]
# Output: [2,3]

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        temp = curr.next

        while curr.next and temp.next:
            if temp.val == temp.next.val:
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                curr.next = temp.next
                temp = curr.next
            else:
                curr = curr.next
                temp = curr.next

        return dummy.next


        

        