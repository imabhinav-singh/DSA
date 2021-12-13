# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        else:
            temp_1 = head
            temp_2 = head.next
            if temp_2 == None:
                return head
            else:
                temp_3 = temp_2.next
                temp_1.next = None            
                while temp_2 != None:
                    temp_2.next = temp_1
                    temp_1 = temp_2
                    temp_2 = temp_3
                    temp_3 = None if temp_3 == None else temp_3.next
                head = temp_1
                return head        