# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
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
        