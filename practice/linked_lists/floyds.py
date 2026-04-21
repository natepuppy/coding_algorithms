

# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def floyds(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

# Create a cycle for cycleStart
d.next = b
print(Solution().floyds(a).val)
