class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addNTwoNumbers(l1, l2):
    temp, l = l1,l2
    c = 0
    resultNode = ListNode((temp.val + l.val + c) % 10)
    c = (temp.val + l.val + c) / 10  
    resultNodetemp = resultNode
    l = l.next
    temp = temp.next     
    while temp != None and l != None:
        val = (temp.val + l.val + c) % 10
        resultNodetemp.next = ListNode(val) 
        resultNodetemp = resultNodetemp.next
        c = (temp.val + l.val + c) / 10
        temp = temp.next
        l = l.next
    while temp != None:
        resultNodetemp.next = ListNode((temp.val + c) % 10)
        c = (temp.val + c) / 10
        resultNodetemp = resultNodetemp.next
        temp = temp.next
    while l != None:
        resultNodetemp = ListNode((l.val + c) % 10)
        c = (l.val + c) / 10
        resultNodetemp = resultNodetemp.next
        l = l.next
    
    if c != 0:
        resultNodetemp.next = ListNode(c)
        
    return resultNode
        
        