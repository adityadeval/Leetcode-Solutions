# Leetcode problem : 141. Linked List Cycle
# Problem description : https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Handling edge case where empty Linked List is given.
        if not head:
            return False
        
        slow = head
        fast = head.next
        # The first condition (while fast) is used to stop the loop when 
        # there isn't a cycle, so fast would eventually become None.
        # Note: We include fast.next as well in the condition as inside the loop we
        # are calculating fast.next.next. So if fast.next is None, then performing
        # fast.next.next would lead to an error.
        # The second condition (slow != fast) is used to break the loop when there is
        # a cycle, so fast and slow would eventually point to the same node.
        while(fast and fast.next and slow != fast):
            slow = slow.next
            fast = fast.next.next

        # Here we check what led to breaking out of the loop. If slow wasn't equal 
        # to fast, then definately the reason for the break would be that fast 
        # became None after traversing through the linked list (which didn't have a
        # cycle). If slow == fast, then there is definately a cycle.
        if slow == fast:
            return True
        else:
            return False
