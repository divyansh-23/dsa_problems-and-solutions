'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

	#the solution using bit manipulation and the only solution which can be done without using any space.
        #time complexity = O(n) and space is O(1)
        
	a = 0
        for x in nums:
            a ^= x
        return a




'''
Approach : Bit Manipulation


Concept:

If we take XOR of zero and some bit, it will return that bit
	a⊕0=a

If we take XOR of two same bits, it will return 0
	a⊕a=0


a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

So we can XOR all bits together to find the unique number.

'''



