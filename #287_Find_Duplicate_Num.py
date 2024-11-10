# Leetcode problem : 287. Find the Duplicate Number
# Problem description : https://leetcode.com/problems/find-the-duplicate-number/description/

# nums contains n+1 integers and these integers are in range[1,n] inclusive.
        # So for eg. if nums contains 10 integers, all numbers would be between:
        # 1 and len(nums)-1 that is 10-1 = 9.
        # So every number in 'nums' won't exceed the highest index of nums.
        #                 0  1  2  3  4  5  6  7  8  9
        # For eg. nums = [6, 7, 9, 8, 9, 3, 2, 4, 1, 5]
        # We can construct a LinkedList such that value of given array would be used as index of nums 
        # to find another value. We then connect these two values.
        # For above eg: 6 -> 2 -> 9 -> 5 -> 3 -> 8 -> 1 -> 7 -> 4
        #                         |                             |
        #                         | _ _ _ _ _ _ _ _ _ _ _ _ _ _ |    
        # Note: This can be done only due to the given conditions. Without that it won't be possible
        # For eg. If nums = [1, 2, 3, 100, 101]. Here len(nums)-1 = 4. But range is not [1, 4] inclusive.

        slow, fast = nums[0], nums[0]
        # 6 -> 2 -> 9 -> 5 -> 3 -> 8 -> 1 -> 7 -> 4
        # slow      |                             |
        # fast      | _ _ _ _ _ _ _ _ _ _ _ _ _ _ | 
        slow = nums[slow]
        fast = nums[nums[fast]]
        # 6  -> 2  -> 9  -> 5  -> 3  -> 8  -> 1  -> 7  -> 4
        #      slow  fast                                 |
        #             |                                   |
        #             | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ | 
        while(slow != fast):
            # For current example, writing slow = nums[slow] is equivalent to slow = slow.next
            # Similarly, nums[nums[fast]] is same as fast = fast.next.next
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 6  -> 2  -> 9  -> 5  -> 3  -> 8  -> 1  -> 7  -> 4
        #             |                            slow   |
        #             | _ _ _ _ _ _ _ _ _ _ _ _ _ _fast_ _| 
        # At this point, the intersection point of slow and fast has been found (7). But that's not the 
        # beginning of the cycle.

        # We initialize slow2 at the beginning, then move slow and slow2 by 1 node each time.
        # Their point of intersection is going to be the beginning of the cycle.
        # The beginning of the cycle is going to be the 'repeated number' in current case.
        slow2 = nums[0]
        # 6  -> 2  -> 9  -> 5  -> 3  -> 8  -> 1  -> 7  -> 4
        #slow2        |                            slow   |
        #             | _ _ _ _ _ _ _ _ _ _ _ _ _ _fast_ _| 
        while(slow2 != slow):
            slow2 = nums[slow2]
            slow = nums[slow]
        # 6  -> 2  -> 9  -> 5  -> 3  -> 8  -> 1  -> 7  -> 4
        #           slow2                          fast   |
        #            slow                                 |
        #             | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _| 
        return slow2
