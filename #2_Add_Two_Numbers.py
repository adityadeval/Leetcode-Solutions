# Leetcode problem : 2. Add Two Numbers
# Problem description : https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        left = dummy
        carry = 0
        # We use 'or' as, in case the length of l1 and l2 are different (for eg: 42, 965), at a certain point we 
        # might have visited all digits of one number, but not all of the other number. So we need to perform all 
        # steps (which create a new node in result list) till we finish visiting all digits of the other number. 
        # We add carry as well in the condition as, in some cases, we might have finished visiting all digits of
        # both numbers, but a carry might be generated and we need to create a new node for this carry.
        # For eg. 42 + 65, when written in reverse order for current problem:
        # num1:   2 --> 4
        # num2:   5 --> 6
        # Result: 7 --> 0 --> 1 (carry)
        while(l1 or l2 or carry):
            if l1: num1 = l1.val
            else: num1 = 0
            if l2: num2 = l2.val
            else: num2 = 0
            result = num1 + num2 + carry

            # Performing % 10 gives us the last digit of the number. This value would be stored in the new node
            # we create as part of the result list.
            new_node_val = result % 10
            # Performing // 10 removes last digit of the number. This value would be the carry.
            carry = result // 10

            # Create a new node with value calculated above. 
            new_node = ListNode()
            new_node.val = new_node_val
            # left pointer always points to an earlier node. Make it's next point to the newly created node.
            left.next = new_node
            left = left.next
            
            # Only if l1 and l2 are not None, advance them further.
            if l1:  l1 = l1.next
            if l2:  l2 = l2.next
        
        return dummy.next
