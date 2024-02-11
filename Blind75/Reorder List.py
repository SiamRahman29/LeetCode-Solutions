# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    if not head:
        return None
    
    def length_count(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    if length_count(head) == 1:
        return head
    
    def halve(head):
        half = length_count(head)//2
        count = 1
        
        first_head = head
        curr = head
        while True:
            if count == half:
                second_head = curr.next
                curr.next = None
                break
            curr = curr.next
            count += 1
        return second_head
    
    def rev(head):
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    second_head = halve(head)
    second_head = rev(second_head)

    while head or second_head:
        #print(head)
        if not head.next:
            head.next = second_head
            break
        else:
            curr = head.next
            head.next = second_head
            head = curr
            second_curr = second_head.next
            second_head.next = head
            second_head = second_curr
