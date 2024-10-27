# Leetcode problem : 143. Reorder List
# Problem description : https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Proceed only if there are at least 2 nodes.
        if head.next:
            # Proceed only if there are at least 3 nodes. We can't directly write this condition
            # as, in case there's only 1 node, it'll give an error.
            if head.next.next:
                # PART 1 : Finding middle node. 
                # The position of slow exactly when fast points to the last element(for an even list)
                # or when fast points to None (for a list with odd number of nodes), would be the 
                # middle node.
                slow = head
                fast = slow.next
                while(fast != None and fast.next != None):
                    fast = fast.next.next
                    slow = slow.next

                # PART 2 : Breaking the list into two halves
                # To break the list into two halves, we point the middle node to None. We 'reverse' the
                # nodes beyond the middle node, and make the node after middle point to None as well.
                # So 1 --> 2 --> 3 --> 4 --> 5 becomes:
                # 1 --> 2 --> 3 --> None and None <-- 4 <-- 5
                # Here, 'slow' is the middle node. So this is how it looks:
                # Node1 --> Node2 --> Node3 -->.....--> Node4 --> Node5 --> Node6 --> Node7,....NodeN
                #                                       slow       p1        p2        p3
                p1 = slow.next
                p2 = slow.next.next
                slow.next = None
                p1.next = None
                #                                       None    None
                #                                         ^       ^
                #                                         |       |
                # Node1 --> Node2 --> Node3 -->.....--> Node4   Node5 --> Node6 --> Node7,....NodeN
                #                                       slow      p1        p2        p3
                
                # PART 3 : Reversing second half
                while(p2):
                    # We'll make p2 point to p1. But before, we need to 'record' what was next to p2.
                    # So we first make p3 point to the next node. 
                    p3 = p2.next
                    p2.next = p1
                    #                                      None    None
                    #                                       ^       ^
                    #                                       |       |
                    # Node1 --> Node2 --> Node3 -->...--> Node4   Node5 <-- Node6 --> Node7...--> NodeN
                    #                                      slow     p1       p2        p3
                    # Now advance p1 and p2.
                    p1 = p2
                    p2 = p3
                    #                         None    None
                    #                          ^       ^
                    #                          |       |
                    # Node1 --> Node2 ...--> Node4   Node5 <-- Node6 --> Node7 --> Node8...--> NodeN
                    #                        slow               p1       p2,p3

                # PART 4 : Generating the Final re-ordered list
                # Here left 1 points to a node from first half. left2 would be just ahead of left1.
                # After reversing the second half is done, p1 would be pointing to last node of 2ndhalf
                # right1 would now point to this last node of the second half.
                # right2 would be just ahead of right1 (to the left of right1 since the list    
                # is reversed).
                left1 = head
                right1 = p1           
                
                while right1:
                    left2 = left1.next
                    right2 = right1.next
                    #                         None    None
                    #                          ^       ^
                    #                          |       |
                    # Node1 --> Node2 ...--> Node4   Node5 <-- Node6 <-- Node7 <-- Node8
                    # left1     left2                                    right2    right1 
                    
                    left1.next = right1
                    right1.next = left2

                    left1 = left2
                    right1 = right2
