class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def floyds(head):
    if not head or not head.next:
        return None
    
    fast, slow = head, head
    has_cycle = False

    # Note: Not fast.next.next...
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            has_cycle = True
            break
    
    if not has_cycle:
        return None
    
    slow2 = head

    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    
    return slow


# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

# Create a cycle for cycleStart
d.next = b
print(floyds(a).val)
