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

#not a good solution but pass all test cases, improve this

'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
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
'''

# Copied solutions but informative

# Two Python Solutions and Explanation of Python Modulo and Int Division Differences From C/Java

# Solution 1: Similar Approach to the official solution, but modified to work with python modulo and division differences

def reverse_v1(self, x: int) -> int:
        reverse = 0
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)
        
        while x != 0:   
            # Python modulo does not work the same as c or java. It always returns the same
            # sign as the divisor and rounds towards negative infinit. Also // rounds towards negative infinity not 0 as in C so this also
            # behaves differently. Python 3.7 added a math.remainder(), but leet code is
            # running a python version prior to this (at least at the time of writing). Since the C 'remainder' behavior is desirable for
            # this problem, the following code emulates it. 
            #
            # See https://stackoverflow.com/questions/1907565/c-and-python-different-behaviour-of-the-modulo-operation and
			# http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
            pop = x % 10 if x >= 0 else (abs(x) % 10)*-1
            x = x // 10 if x >=0 else math.ceil(x / 10)

            if (reverse > max_int//10) or (reverse == max_int // 10 and pop > 7):
                return 0
            
            if (reverse < math.ceil(min_int / 10)) or (reverse == math.ceil(min_int / 10) and pop < -8):
                return 0
            
            reverse = reverse * 10 + pop
        
        return reverse



'''
Solution 2: Using string as an intermediate representation.

However, in this solution, there is one loophole, we are checking at the end that if the "result" is in the range allowed i.e. if the result is smaller
than the max_int and bigger than the min_int.
But in the question,its written that "the environment does not allow you to store the 64 bit integers i.e. greater than 32 bit integers. And in this solution,
we already store the number which can be out of this range in the "result" and then check if it is out of range or not. 
But, this solution works perfectly on leetcode. 
And is kind of the approach I took with my first original solution.
 

def reverse_v2(self, x: int) -> int:
	max_int = pow(2, 31)-1
	min_int = pow(-2, 31)

	str_x = str(abs(x))
	str_x_reversed = str_x[::-1]
	result = int(str_x_reversed)
	result = result * -1 if x < 0 else result

	return result if (result < max_int and result > min_int) else 0
'''





