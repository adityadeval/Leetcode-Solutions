# Leetcode problem : 567. Permutation In String
# Problem description : https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # String s2 should use its characters to create String s1.
        # However, if s2 is smaller, it definately won't have enough chars to make s1.
        if len(s1) > len(s2):
            return False

        # Both below dictionaries will be used to store 26 keys ('a' to 'z'). 
        # Value of these keys would be freq. of those characters in the respective strings.
        # char_match would store how many corresponding keys have same values in both dict.
        # For eg. If s1 has 4 'a's, 3 'b's, 6 'c's, 0 'd's, 0 'e's, ......, 0 'z's
        #            s2 has 4 'a's, 1 'b',  6 'c's, 0 'd's, 0 'e's, ......, 0 'z's
        # then char_match would be 2.
        s1_dict = dict()
        s2_dict = dict()
        char_match = 0

        # Initialize both dictionaries with keys 'a' to 'z' and values = 0.
        for c in range(ord('a'), ord('z')+1):
            s1_dict[chr(c)] = 0
            s2_dict[chr(c)] = 0

        # Now we create a sliding window of size = length of string s1.
        # After this for loop ends, the first sliding window would be ready. 
        # This sliding window will cover all characters of string s1. We'll add the count
        # of all characters in this window into s1_dict.
        # The same sliding window would cover the first 'n' characters of string s2 and 
        # we'll add their count into s2_dict. ('n' is the length of string s1).
        left, right = 0, 0
        for right in range(0, len(s1)):
            s1_dict[s1[right]] += 1
            s2_dict[s2[right]] += 1

        # Once both dicts are ready, we'll compare their respective keys, to determine
        # 'char_match' which stores how many corresponding keys have their values in sync.
        # If all 26 keys have same values, it means we have found the part of String s2 which
        # is a permutation of String s1.
        for c in s1_dict:
            if s1_dict[c] == s2_dict[c]:
                char_match += 1
        if char_match == 26:
            return True

        # If we reach here, it means the characters in the sliding window above pointed on
        # String s2 aren't a permutation of s1. So we need to slide the window ahead.
        while right < len(s2):
            # Sliding the window ahead = 'Removing char at left' AND 'Adding char at right+1'
            # Everything in between stays as it is

            # Below part deals with 'Removing char at left'
            # We reduce the count of whatever character is present at the left pointer.
            s2_dict[s2[left]] -= 1
            # After reducing the count of that character in s2_dict, if it becomes equal to
            # the count of the same character in s1_dict, then we have found a match.
            if s2_dict[s2[left]] == s1_dict[s2[left]]:
                char_match += 1
            # If below 'if' is true, it means, the count of that character was originally
            # same in both dictionaries. But this action of moving left pointer ahead made
            # the counts of it unequal. So we reduce char_match by 1.
            elif s2_dict[s2[left]] + 1 == s1_dict[s2[left]]:
                char_match -= 1
            # Finally, after we have successfully dealt with the effects of moving left 
            # pointer ahead, we then actually move it ahead. 
            left += 1

            # Below code deals with 'Adding char at right+1' part of sliding the window ahead
            # We first move the right pointer ahead.
            right += 1
            if not right == len(s2):
                # We increase count of whatever character is present at the new position
                # of right pointer.
                s2_dict[s2[right]] += 1
                # After updating this count in s2_dict, if it becomes equal to that of 
                # s1_dict, it means we have found another match.
                if s2_dict[s2[right]] == s1_dict[s2[right]]:
                    char_match += 1
                # In case below if is true, it means, before adding this new character in the
                # window, the counts of the same character in both windows was equal, but now
                # they're not equal. So we reduce char_match.
                elif s2_dict[s2[right]] - 1 == s1_dict[s2[right]]:
                    char_match -= 1
            
            # At this point we've successfully slided the window(of fixed size) ahead by
            # 1 position. Before sliding it further ahead in the next iteration of while 
            # loop, check if all 26 characters have same counts in both dicts.
            if char_match == 26:
                return True
        
        # At this point we're out of the while loop and the sliding window has reached the
        # end of String s2.
        return False        
