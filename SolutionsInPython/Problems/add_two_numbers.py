class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My solution
def addNTwoNumbers(l1, l2):
    temp, l = l1,l2
    c = 0
    resultNode = ListNode((temp.val + l.val + c) % 10)
    c = (temp.val + l.val + c) / 10  
    resultNodetemp = resultNode    
    while temp.next != None and l.next != None:
        val = (temp.next.val + l.next.val + c) % 10
        resultNodetemp.next = ListNode(val) 
        resultNodetemp = resultNodetemp.next
        c = (temp.next.val + l.next.val + c) / 10
        temp = temp.next
        l = l.next
    while temp.next != None:
        resultNodetemp.next = ListNode((temp.next.val + c) % 10)
        c = (temp.next.val + c) / 10
        resultNodetemp = resultNodetemp.next
        temp = temp.next
    while l.next != None:
        resultNodetemp.next = ListNode((l.next.val + c) % 10)
        c = (l.next.val + c) / 10
        resultNodetemp = resultNodetemp.next
        l = l.next
    while c != 0:
        resultNodetemp.next = ListNode(c % 10)
        c = c / 10
        resultNodetemp = resultNodetemp.next
        
    return resultNode

# Referenced solution 

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        # new digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)
        # update ptrs
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
    


        