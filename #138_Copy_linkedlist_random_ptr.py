# Leetcode problem : Copy Linked List with Random Pointer
# Problem description : https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Run: O(n), Space: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # PART 1: Create a new node as part of the new list and interweave the nodes of 
        # the old and copied list. If Old List: A --> B --> C --> D then after 
        # the while loop ends, the interWeaved List: 
        # A --> A' --> B --> B' --> C --> C' --> D --> D'
        # Below pointer can be read as 'current pointer of Old list'.
        curr_old_list = head
        while(curr_old_list):
            # Create a new node as part of the new list. We initialize it's next
            # and random pointers with None as the remaining nodes don't exist yet.
            val_copy = curr_old_list.val
            # Below pointer can be read as 'current pointer of new list'.
            curr_new_list = Node(val_copy, None, None)
            # right_old_list would always stay one node ahead of the curr_old_list.
            right_old_list = curr_old_list.next
            curr_old_list.next = curr_new_list
            curr_new_list.next = right_old_list
            curr_old_list = right_old_list

        # PART 2: Make the 'random' pointers of the new list point to the correct nodes of
        # the new list.
        curr_old_list = head
        while(curr_old_list):
            curr_new_list = curr_old_list.next
            if curr_old_list.random == None:
                curr_new_list.random = None
            else:
                # Each time we access 'next' of any node from the old_list, we are
                # definitely going to get a node of the new list.
                # Due to this, when we write curr_old_list.random and access it's next,
                # we're going to get a node of the new_list. 
                # Now all we have to do is make the random pointer of our new list's 
                # current node, point to it.
                random_finder = curr_old_list.random.next
                curr_new_list.random = random_finder
            # We can't directly move to the next node in the old_list by simply writing
            # next. We have to pass through the new_list to access the next node of the 
            # old list, due to the interweaving.
            curr_old_list = curr_old_list.next.next

        # PART 3 : Remove the interweaving. Next of each node in new_list MUST point to 
        # another node from new_list itself. Also, although not mandatory, reset the old
        # list as well to it's original state.
        head_new_list = head.next
        curr_old_list = head
        curr_new_list = head_new_list
        while(curr_new_list.next):
            curr_old_list.next = curr_new_list.next
            curr_new_list.next = curr_new_list.next.next
            curr_old_list = curr_old_list.next
            curr_new_list = curr_new_list.next

        return head_new_list
