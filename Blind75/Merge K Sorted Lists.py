# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(self, lists):
    if lists == [] or lists == [[]]:
        return None
    all_values = []
    for i in range(len(lists)):
        head = lists[i]
        while head:
            all_values.append(head.val)
            head = head.next
    all_values.sort()
    all_values.reverse()
    curr = dummy = ListNode()
    while len(all_values) > 0:
        curr.next = ListNode(all_values.pop())
        curr = curr.next
        
    return dummy.next
