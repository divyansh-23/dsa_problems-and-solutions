/*
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
*/

// this is the follow up solution where the space is constant i.e. O(1)

//Time: O(n) and Space O(1)
class Solution {
public:
    string reverseWords(string s) {
        int left1 = 0, right1 = s.length() -1;
        while (left1 < right1){
            swap(s[left1], s[right1]);
            left1++;
            right1--;
        }

        int start = 0, n = s.length(), index= 0;
        for(start = 0; start < n; start++){
            if (s[start] != ' ') {

                if (index != 0) s[index++] = ' ';

                int end = start;
                while(end < n && s[end] != ' ') s[index++] = s[end++];

                reverse(s.begin() + index - (end-start), s.begin() + index);
                start = end;
            }
        }

        s.erase(s.begin() + index, s.end());
        return s;
    }
};

