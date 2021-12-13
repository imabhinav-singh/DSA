# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def negateList(self, head: ListNode) -> ListNode:
        temp = head
        while temp != None:
            temp.val = -temp.val
            temp = temp.next
        return head
            
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headA = self.negateList(headA)
        temp = headB
        while temp != None and temp.val >= 0:
            temp = temp.next
        headA = self.negateList(headA)
        return temp