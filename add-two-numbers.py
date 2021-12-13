# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result, head = None, None
        carry = 0
        while l1 != None and l2 != None:
            if result == None:
                result = ListNode((carry + l1.val + l2.val)%10, None)
                head = result
            else:
                result.next = ListNode((carry + l1.val + l2.val)%10, None)
                result = result.next
            carry = int((carry + l1.val + l2.val)/10)
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            result.next = ListNode((carry + l1.val)%10, None)
            result = result.next
            carry = int((carry + l1.val)/10)
            l1 = l1.next
            
        while l2 != None:
            result.next = ListNode((carry + l2.val)%10, None)
            result = result.next
            carry = int((carry + l2.val)/10)
            l2 = l2.next
            
        if carry != 0:
            result.next = ListNode(carry, None)
        
        return head