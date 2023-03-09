'''
260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]

'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # difference between two numbers (x and y) which were seen only once

        bitmask = 0
        for num in nums:
            bitmask ^= num

        # rightmost 1-bit diff between x and y

        diff = bitmask & (-bitmask)

        #use this x as x_bitmask which is to find x
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num

        #now since bitmask will contain both x and y. get y out of bitmask
        y = bitmask ^ x 

        return [x, y]            

