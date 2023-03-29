/*
540. Single Element in a Sorted Array


You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
*/

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        bool even = false;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (middle % 2 == 1) {
                middle = middle - 1;
            }
            if (left == right) {
                return nums[left];
            } else if (nums[middle] != nums[middle + 1]){
                right = middle;
            } else {
                left = middle + 2;
            }
        }
        return -1;
    }
};

/* 
Approach for this Problem:
Initialize two pointers, left and right, to the first and last indices of the input array, respectively.
While the left pointer is less than the right pointer:
a. Compute the index of the middle element by adding left and right and dividing by 2.
b. If the index of the middle element is odd, subtract 1 to make it even.
c. Compare the middle element with its adjacent element on the right:
i. If the middle element is not equal to its right neighbor, the single element must be on the left side of the array, so update the right pointer to be the current middle index.
ii. Otherwise, the single element must be on the right side of the array, so update the left pointer to be the middle index plus 2.
When the left and right pointers converge to a single element, return that element.

Time complexity: O(log n/2) = O(log n)
Space: O(1)
*/



