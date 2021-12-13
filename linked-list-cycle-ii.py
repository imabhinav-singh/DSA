# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        else:
            temp = head
            start = None
            while temp.next != None:
                temp.val = 1000000 + temp.val if temp.val >= 0 else -1000000 + temp.val
                temp = temp.next
                if temp.val < -100000 or temp.val > 100000:
                    start = temp
                    break
            temp = head
            while temp.val < - 100000 or temp.val > 100000:
                temp.val = -1000000 + temp.val if temp.val >= 0 else 1000000 + temp.val
                temp = temp.next
            return start
            