def addNTwoNumbers(l1, l2):
    temp, l = l1,l2
    resultNode = l1.val + l2.val
    c = 0
    
    
    while temp != None and l != None:
        resultNode.next = temp.val + l.val
        temp = temp.next
        l = l.next
        resultNode = resultNode.next
        
        
        
# Not yet completed. To Do