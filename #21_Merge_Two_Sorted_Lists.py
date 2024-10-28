# Leetcode problem : 21. Merge Two Sorted Lists
# Problem description : https://leetcode.com/problems/merge-two-sorted-lists/description/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        # curr is always going to point to the node that is 'recently' added to the 'under construction'
        # merged list. 
        # Think of curr as someone who'll observe which is lower, node pointed by list1 or node pointed by 
        # list2. Once identified, it'll then:
        # 1) Construct a path from itself to the lower node, cutting of any other path going out from it
        # 2) Jump onto the lower node
        # 3) Push the pointer (list1 or list2) ahead who pointed to that space originally.
        curr = dummy_node
        
        # curr is going to keep pushing pointers list1 and list2 ahead, until one of them goes beyond the
        # last node and start pointing to None (since last_node.next = None). 
        # Below while loop exits, as soon as this happens.
        while(list1 and list2):
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        # At this point we determine, which linked list has all of its nodes added. If we reached end of
        # linkedlist1, then we make the last node of it point to the 'latest' node of linkedlist2 (node
        # pointed by list2).
        # 'latest' means the node of list2 right after a node of list2 that was added to our merged list. 
        # For eg. If 1 --> 1 --> 2 --> 3 --> 4 (of list 1) have been added.
        # Now the 'latest' element of list2 would be node 4. 
        # Note that we do not have to traverse beyond the Node 4 of list 2, as the lists are
        # already sorted in ascending order. So we just return the head.

        if not list1:
            curr.next = list2
            return dummy_node.next
        if not list2:
            curr.next = list1
            return dummy_node.next
