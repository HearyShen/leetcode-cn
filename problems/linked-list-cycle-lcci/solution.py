# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """Slow-Fast pointer algorithm for cycle detection."""
        # detect cycle with slow-fast pointer
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                break
        
        # if no-cycle until while-loop finished, then no-cycle in linked-list
        if not fast_ptr or not fast_ptr.next:
            return None
        else:
            # move one-step forward per time, 
            # eventually meet at cycle start node.
            slow_ptr = head
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
            return slow_ptr
        
