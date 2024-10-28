# Leetcode problem : 19. Remove Nth Node From End of List
# Problem description : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        curr_node = head
        # Note that we're given condition 1 <= n <= sz(Total number of nodes).
        # So 'n' at the most can be equal to total number of nodes and not more than it.

        # If there were only 'n' nodes in the list, the node to be removed would be the head.
        # So we first move the curr_node pointer (n-1) times. Note that it's already at node1.
        # So basically it is at 1 and we'll be adding 1 to it (n-1) times:
        # Final position = 1 + 1(n-1) = n. 
        for i in range(n-1):
            curr_node = curr_node.next
        
        # Once curr_node has reached 'n'th node, then we can set target_node to head.
        # target_node would eventually point to the node we'll delete.
        prior_to_target = None
        target_node = head

        # Run below while loop to advance the pointer target_node.
        # This should run ONLY if total number of nodes > n.
        # If total number of nodes == n then we need to remove the head itself and target
        # is already pointing at head. So no need to move the target pointer.
        while(curr_node.next):
            curr_node = curr_node.next
            prior_to_target = target_node
            target_node = target_node.next
        
        # Below 'if' becomes True only if total number of nodes == n as in this case pointers
        # target_node and prior_to_target would not be moved forward.
        if prior_to_target == None:
            # Since we're deleting the head, we create a new head.
            new_head = target_node.next
            target_node.next = None
            return new_head
        else:
            # Here the head of our resulting list remains the same.
            prior_to_target.next = target_node.next
            target_node.next = None
            return head
