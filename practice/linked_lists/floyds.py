

# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def floyds(self, head):
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break
        
        # Can do this with the else on the while loop instead...
        if not fast or not fast.next:
            return None
        
        slow_2 = head
        while slow != slow_2:
            slow = slow.next
            slow_2 = slow_2.next
        
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


















'''

class Solution:
    def floyds(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else: # Executed when the while criteria is not met anymore, but not when a break is hit.
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

'''