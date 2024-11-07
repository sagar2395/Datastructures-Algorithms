# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY


from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        while headA and headB:
            if headA == headB:
                return headA
            elif headA in visited:
                return headA
            elif headB in visited:
                return headB
            else:
                visited.add(headA)
                headA = headA.next
                visited.add(headB)
                headB = headB.next

        if headA:
            while headA:
                if headA in visited:
                    return headA
                headA = headA.next
        elif headB:
            while headB:
                if headB in visited:
                    return headB
                headB = headB.next


        return None

