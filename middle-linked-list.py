# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mid = head
        temp = head
        while temp != None and temp.next != None:
            mid = mid.next
            temp = temp.next.next
        return mid