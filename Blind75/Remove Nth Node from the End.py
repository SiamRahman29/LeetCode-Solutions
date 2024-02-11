# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    if not head:
        return None
    
    def length_count(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    l = length_count(head)

    target = l - n
    
    def del_node(target,head):    
        
        prev = head
        curr = prev.next
        if target == 0:
            
            prev.next = None
            return curr
        position = 1
        while curr.next:
            if position == target:
                prev.next = curr.next
                curr.next = None
                
                return head
            prev = curr
            curr = curr.next
            position += 1
        
        prev.next = None
        return head
    result = del_node(target,head)
    
    return result
