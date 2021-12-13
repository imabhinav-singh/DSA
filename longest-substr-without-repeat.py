class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        sub_str = "" + s[0]
        max_len = 1
        temp_len = 1
        for i in range(1, len(s)):
            idx = sub_str.find(s[i])
            if idx == -1:
                sub_str += s[i]
                temp_len += 1
            else:
                max_len = max(max_len, temp_len)
                sub_str = sub_str[idx+1:] + s[i]
                temp_len = len(sub_str)
                
        max_len = max(max_len, temp_len)        
        return max_len
        