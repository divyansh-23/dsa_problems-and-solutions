'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


#solution'''

class Solution(object):
    def sortColors(self, nums):
        i = 0
        zero_at = 0
        two_at = len(nums) - 1
        while i <= two_at:
            if nums[i] == 0:
                nums[i], nums[zero_at] = nums[zero_at], nums[i]
                i += 1
                zero_at += 1
            elif nums[i] == 2:
                nums[i], nums[two_at] = nums[two_at], nums[i]
                two_at -= 1
            else:
                i += 1
