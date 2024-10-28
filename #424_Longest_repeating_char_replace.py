# Leetcode problem : 424. Longest Repeating Character Replacement
# Problem description : https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        # Stores final answer
        max_length = 0
        # Dictionary for storing frequency of characters "in current window only".
        freq_dict = dict()

        for right in range(len(s)):
            freq_dict[s[right]] = freq_dict.get(s[right], 0) + 1

            # Window size = (right - left + 1)
            # Highest frequency in current window = max(freq_dict.values())
            # The result of below subtraction gives us number of characters that are 
            # causing a problem. We can replace only 'k' number of characters. 
            # So in case number of replacements needed > k, we'll shrink the window.
            while (right - left + 1) - max(freq_dict.values()) > k:
                    freq_dict[s[left]] = freq_dict[s[left]] - 1
                    # Note that left pointer is moved ahead AFTER updating frequency
                    # of character pointed by left.
                    left += 1
            
            # At this point either the while loop wasn't executed or it finished its 
            # execution. In both cases, we'll be left with a VALID window, that is one
            # having the same characters except a few but they aren't more than k.
            # We compare the length of this window with the earlier longest VALID 
            # window and update max_length if required.
            max_length = max(max_length, right - left + 1)

        return max_length
