"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        copy = {}
        newHead = Node(head.val, None, None)
        temp = head.next
        copy[head] = newHead
        newTemp = newHead
        while temp != None:
            newTemp.next = Node(temp.val, None, None)
            newTemp = newTemp.next
            copy[temp] = newTemp
            temp = temp.next
        temp = head
        newTemp = newHead
        while temp != None:
            if temp.random != None:
                newTemp.random = copy[temp.random]
            temp = temp.next
            newTemp = newTemp.next
        return newHead