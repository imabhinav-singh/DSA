# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        '''
        if head == None:
            return False
        else:
            temp = head
            while temp.next != None:
                temp.val = 1000000 + temp.val if temp.val >= 0 else -1000000 + temp.val
                temp = temp.next
                if temp.val < -100000 or temp.val > 100000:
                    return True
            return False
        '''