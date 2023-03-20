'''
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        '''
        #solution 1: my own solution-- not clean and well optimized but covers all edge cases and is linear.

        length = len(flowerbed)
        count = 0
        if length == 0:
            return False
        elif length == 1:
            if flowerbed[0] == 0:
                count += 1
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                count += 1
            if length == 2: return count >= n

            for i in range(1, len(flowerbed) - 1):
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1

            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] == 1
                count += 1
            
        if count >= n:
            return True
        
        return False
        '''

        #cleaner and more optimised solution

        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_pocket = i == 0 or flowerbed[i-1] == 0
                right_pocket = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

                if left_pocket and right_pocket:
                    flowerbed[i] = 1
                    count += 1

                    if count == n:
                        #ending the loop and returning True once the count becomes equal to given "n", thus saving
                        # time on iterating through the remaining values in the array
                        return True
        
        return count >= n


	# COMPLEXITY = TIME: O(n), Space: O(n)



