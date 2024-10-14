class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def mergeSortedList(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        curr.next = l1 if v1 < v2 else l2
        curr = curr.next    
    
    return dummy.next

# Currently working
        