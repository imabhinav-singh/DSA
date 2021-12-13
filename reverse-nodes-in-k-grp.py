class Solution:
    def checkK(self, head: ListNode, k: int) -> bool:
        i = 1
        temp = head
        while i<=k and temp != None:
            temp = temp.next
            i += 1        
        return False if i <= k else True
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prevgrp = None       
        next = head
        while self.checkK(next, k):
            prev = None
            grpfirst = next
            for i in range(k):
                temp = next.next
                next.next = prev
                prev = next
                next = temp
            grpfirst.next = next
            if prevgrp == None:
                head = prev
            else:
                prevgrp.next = prev
            prevgrp = grpfirst
        return head