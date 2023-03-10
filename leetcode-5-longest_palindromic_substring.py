'''
5. Longest Palindromic Substring

Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''


# Time O(n) and space O(1)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Approach - Expand Around Center
        if s is None or len(s) < 1:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)

            length = max(len1, len2)
            

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end+1]

    def expandAroundCenter(self, s, left, right):
        L, R = left, right

        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        return R - L - 1




