class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        seen = {}

        for end in range(len(s)):
            # If character already seen and its index is within the current window
            if s[end] in seen and seen[s[end]] >= start:
                start = seen[s[end]] + 1  # Move start right after the duplicate

            # Update the last index of current character
            seen[s[end]] = end

            # Update max_len for current window
            max_len = max(max_len, end - start + 1)

        return max_len
