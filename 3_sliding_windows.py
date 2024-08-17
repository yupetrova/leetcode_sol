class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left_pos = 0    #початок вікна
        unique_set = set()

        for right_pos in range(len(s)):
            while s[right_pos] in unique_set:
                unique_set.remove(s[left_pos])
                left_pos += 1
            unique_set.add(s[right_pos])
            result = max(result, right_pos - left_pos + 1)      #кінець вікна - початок вікна
        
        return result
    
