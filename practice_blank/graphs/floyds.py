# Find the middle of a linked list with two pointers.
# Time: O(n), Space: O(1)
def middleOfList(head):
    # Code will be implemented here
    return head


# Determine if the linked list contains a cycle.
# Time: O(n), Space: O(1)
def hasCycle(head):
    # Code will be implemented here
    return False


# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)
def cycleStart(head):
    # Code will be implemented here
    return head


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

print(middleOfList(a).val)
print(hasCycle(a))

# Create a cycle for cycleStart
d.next = b
print(cycleStart(a).val)
