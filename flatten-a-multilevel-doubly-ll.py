"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:  
    def flattenUtil(self, head: 'Node', tail: 'Node') -> 'Node':
        if head == None:
            return tail
        tail.next = Node(head.val, None, None, None)
        tail.next.prev = tail
        tail = tail.next
        if head.child != None:
            tail = self.flattenUtil(head.child, tail)
        tail = self.flattenUtil(head.next, tail)
        return tail       
        
    def flatten(self, head: 'Node') -> 'Node':
        result = Node(0, None, None, None)
        tail = result
        self.flattenUtil(head, tail)
        if result.next == None:
            return None
        else:
            result.next.prev = None
            result = result.next
            return result


"""

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:  
    def getTail(self, head: 'Node') -> 'Node':
        temp = head
        while temp.next != None:
            temp = temp.next
        return temp
        
    def flatten(self, head: 'Node') -> 'Node':
        temp = head
        while temp != None:
            if temp.child != None:
                childTail = self.getTail(temp.child)
                temp.child.prev = temp
                childTail.next = temp.next
                if temp.next != None:
                    temp.next.prev = childTail
                temp.next = temp.child
                temp.child = None
            temp = temp.next
        return head
"""

"""
class Solution {
/*Global variable pre to track the last node we visited */
    Node pre = null;
    public Node flatten(Node head) {
        if (head == null) {
            return null; 
        }
/*Connect last visted node with current node */
        if (pre != null) {
            pre.next = head; 
            head.prev = pre;
        }

        pre = head; 
/*Store head.next in a next pointer in case recursive call to flatten head.child overrides head.next*/
        Node next = head.next; 

        flatten(head.child);
        head.child = null;

        flatten(next);        
        return head; 
    }
}
"""