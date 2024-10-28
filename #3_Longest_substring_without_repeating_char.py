# Leetcode problem : 3. Longest Substring Without Repeating Characters
# Problem description : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest_length = 0
        curr_length = 0
        left, right = 0, 0
        
        while right < len(s):
            # Go on adding elements into the set and increasing the curr_length,
            # till a duplicate character is found. Update longest_length if a new max
            # length is found.
            if s[right] not in char_set:
                char_set.add(s[right])
                curr_length += 1
                longest_length = max(longest_length, curr_length)
                right += 1
            # If a duplicate is found, keep right pointer where it is and keep pushing
            # left pointer ahead, till it goes beyond the character which is equal to 
            # the one pointed by right pointer. 
            #                      0 1 2 3 4 5 6 7 8 9
            # For eg. Consider s = d e g f a b c f x y.
            # Now left would be at index 0 (d) and right at index 7 (f) when duplicate 
            # occurs. At this point, keep right pointing to index 7, but keep pushing
            # left ahead till it reaches index 4 (character a).
            # At this point, char_set = {a, b, c} and 'f' won't be added yet. 
            # In the next iteration of the outer while loop, 'f' would get added to 
            # the set.
            else:
                while s[right] in char_set: 
                    char_set.remove(s[left])
                    left += 1
                    curr_length -= 1

        return longest_length
