/*
186. Reverse Words in a String II
Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.
 
Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:
Input: s = ["a"]
Output: ["a"]
 
Constraints:
1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
*/

class Solution {
public:
    void reverseWords(vector<char>& s) {
        //Approach 2: Self written complete(almost same as editorial), Time: O(n), Space: O(1)
        reverse(s.begin(), s.end());

        int start = 0, end = 0, n = s.size();

        for (int i= 0; i < n; i++){
            while (i < n && s[i] != ' '){
                end++;
                i++;
            } 
            reverse(s.begin() + start, s.begin() + end);
            start = i+1;
            end = start;
        }
    }
};

/*
//Approach 1: Just like the Reverse words in a string question. 
class Solution {
public:
    void reverseWords(vector<char>& s) {
        int left1 = 0, right1 = s.size() -1;
        while (left1 < right1){
            swap(s[left1], s[right1]);
            left1++;
            right1--;
        }
        int start = 0, n = s.size(), index= 0;
        for(start = 0; start < n; start++){
            if (s[start] != ' ') {
                if (index != 0) s[index++] = ' ';
                int end = start;
                while(end < n && s[end] != ' '){
                     index++;
                     end++;
                }
                reverse(s.begin() + index - (end-start), s.begin() + index);
                start = end;
            }
        }
    }
};
*/



