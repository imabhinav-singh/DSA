class Solution:            
    def isPalindrome(self, head: ListNode) -> bool:
        reverse = None
        slow = fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            temp = reverse
            reverse = slow
            slow = slow.next
            reverse.next = temp
        
        if fast != None:
            slow = slow.next
        
        while reverse != None:
            if reverse.val != slow.val:
                return False
            reverse = reverse.next
            slow = slow.next
        
        return True