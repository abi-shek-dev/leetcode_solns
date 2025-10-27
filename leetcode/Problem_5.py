def longestPalindrome(s):
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Check for odd-length palindrome
        palindrome1 = expand_from_center(i, i)
        # Check for even-length palindrome
        palindrome2 = expand_from_center(i, i + 1)

        # Update longest
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest
