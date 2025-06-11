class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_try = 0
        char_index = 0
        for char in s:
            char_index += 1
            this_try = 1
            set_char = set()
            set_char.add(char)
            for char2 in s[char_index:]:
                if char2 in set_char: break
                this_try += 1
                set_char.add(char2)
            if this_try > best_try: best_try = this_try
        return best_try

# Awful complexity
# Optimization needed: Skip the chars which were already checked, wasting runtime on sublists that are already known.