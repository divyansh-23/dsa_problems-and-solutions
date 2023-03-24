'''
2348. Number of Zero-Filled Subarrays
Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.
 
Example 1:
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
Example 3:
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.
'''

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #my solution
        output = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i
                while j < len(nums) and nums[j] == 0:
                    j += 1
                n = j - i
                output += n*(n+1)/2
                i = j
            else:
                i += 1    
        return output

        '''Official Solution
            Algorithm
            Initialize ans = 0, numSubarray = 0.
            Iterate over nums, for each number num:
            If num = 0, increment numSubarray by 1.
            Otherwise, set numSubarray = 0.
            Then increment ans by numSubarray.
            Return ans at the end of the iteration.
        ans, num_subarray = 0, 0
        
        for num in nums:
            if num == 0:
                num_subarray += 1
            else:
                num_subarray = 0
            ans += num_subarray
        
        return ans
        '''



