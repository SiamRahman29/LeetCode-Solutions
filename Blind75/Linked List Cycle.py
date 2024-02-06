# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, position):
        self.val = x
        self.next = next
        self.position = 0

def hasCycle(self, head):
    if not head:
        return False

    curr = head

    while curr.next:
        if curr.val == 'Unicorn':
            return True
        curr.val = 'Unicorn'
        curr = curr.next
    return False

