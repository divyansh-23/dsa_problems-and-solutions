'''
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
'''

#not a good solution, improve this

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31 -1 or x < -2 **31:
            return 0
        negative = False
        if x < 0:
            x = abs(x)
            negative = True

        x_array = list(str(x))
        left, right = 0, len(x_array) - 1

        while left < right:
            x_array[left], x_array[right] = x_array[right], x_array[left]
            left += 1
            right -= 1
        
        output = int(''.join(x_array))
        
        if output > 2**31 -1 or output < -2 **31:
            return 0

        return -output if negative else output


