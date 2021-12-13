# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self, head: ListNode, last: ListNode, val):
        if head == None:
            head = ListNode(val, None)
            last = head
            return [head, last]
        else:
            last.next = ListNode(val, None)
            last = last.next
            return [head, last]
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            head, last = None, None
            while l1 != None and l2 != None:
                if l1.val < l2.val:
                    head, last = self.insert(head, last, l1.val)
                    l1 = l1.next
                else:
                    head, last = self.insert(head, last, l2.val)
                    l2 = l2.next
            if l1 != None:
                last.next = l1
            if l2 != None:
                last.next = l2
            return head                        