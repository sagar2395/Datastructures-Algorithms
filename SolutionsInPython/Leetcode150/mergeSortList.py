# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head

        def findMid(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid = findMid(head)

        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        def merge(left, right):
            dummy = ListNode(0)
            temp = dummy
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            
            if left:
                temp.next = left
            if right:
                temp.next = right

            return dummy.next
        return merge(left, right)