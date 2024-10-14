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

        


        