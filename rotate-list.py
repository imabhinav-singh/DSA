# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        n = 0
        temp = head
        while temp != None:
            temp = temp.next
            n += 1
        k = k%n
        if k == 0:
            return head
        else:
            ahead = head
            for i in range(k-1):
                ahead = ahead.next
            behind = head
            prev = None
            while ahead.next != None:
                prev = behind
                behind = behind.next
                ahead = ahead.next
            prev.next = None
            ahead.next = head
            return behind