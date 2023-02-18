/*

7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


*/
//this problem cant be done in python because python can't satisfy this condition "Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."

// so here is the C++ solution


class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX / 10 || ( rev == INT_MAX / 10 && pop > 7 )) return 0;
            if (rev < INT_MIN / 10 || ( rev == INT_MIN / 10 && pop < -8 )) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};

 time-- log X to base 10, since it only will run the number of digits x will have since its getting
//divided by 10 everytime
// Space - O(1)








