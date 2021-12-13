# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        prev = None
        end = head
        for i in range(n-1):
            end = end.next
        
        while end.next != None:
            prev = node
            node = node.next
            end = end.next
        
        if prev == None:
            return node.next
        else:
            prev.next = node.next
            node.next = None
            return head        