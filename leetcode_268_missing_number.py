'''268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # '''
        #Solution 1: Using simple math
        #Complexities: Time: O(n), Space: O(1)
        
        actual_sum = 0
        supposed_sum = 0

        '''we can use Gauss formula to compute the supposed sum without running a loop, so that the time complexity of getting the sum can be brought down from O(n)
        to O(1); however the overall time complexity will still remain O(n)'''
        # supposed_sum = len(nums) * (len(nums) + 1) // 2

        for i in range(len(nums) + 1):
            supposed_sum += i
        
        for x in nums:
            actual_sum += x
        
        return supposed_sum - actual_sum
        '''

        #Solution: 2 - Using bit manipulation
        #Complexities: O(n) time and O(1) space

        missing_num = len(nums)
        for i, value in enumerate(nums):
            missing_num ^= i ^ value
        
        return missing_num

        '''

