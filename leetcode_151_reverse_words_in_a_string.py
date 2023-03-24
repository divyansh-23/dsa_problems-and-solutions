'''
151. Reverse Words in a String
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
 
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 
Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
NOTE: The follow up is solved in C++, and is pushed in the same commit.
'''

# from collections import deque
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        Approach 1: using built in functions reversed and split [Time = O(n), Space = O(n)]
            return ' '.join(reversed(s.split()))
        '''

        #approach 2: using deque [time = O(n), Space = O(n)]

        left, right = 0, len(s) - 1
        #remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        #remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        words_deque = deque()
        word = []

        while left <= right:
            if s[left] == ' ' and word:
                words_deque.appendleft(''.join(word)) # while appending to deque we have to join the elements in the word array since the alphabets are appended as individual elements in the word array
                word = [] # we again have to empty the word array for the new word elements to be inserted here
            elif s[left] != ' ':
                word.append(s[left])
            left += 1

        words_deque.appendleft(''.join(word))
        return ' '.join(words_deque)








