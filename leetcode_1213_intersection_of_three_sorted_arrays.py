'''
1213. Intersection of Three Sorted Arrays


Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Example 2:

Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000

'''

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        '''Brute Force Approach: Time: O(n) and Space: O(n)
        ans = []
        hashMap = collections.Counter(arr1 + arr2 + arr3)
        print(hashMap)
        for item in hashMap:
            if hashMap[item] == 3:
                ans.append(item)
            
        return ans
        '''
        '''
        # Approach 2: Optimised approach with three pointers but this is not ideal

        ans = []
        p1 = p2 = p3 = 0

        while (p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3)):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                ans.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1

        return ans
        '''
        #Approach 3: Binary Search

        '''
        Let's say arr1.length == 5, arr2.length == 10M, arr3.length == 10M. Values in arr1 are larger than most values in other 2 arrays (arr2 and arr3 contain 1..10M and arr1=[10M - 4, 10M - 3, 10M - 2 ,10M - 1, 10M] for example).
in this case 3 pointers solution will perform 20M comparisons, binary search 5 * (2 * log(10M)) ~= 240

When the length of the given arrays are comparable, the Problem provides efficient solution with Three Pointers Approach
When there is a smaller array and a two larger array, the number of comparisons can be significantly reduced if we are using binary search,
        '''

        l, m, n = len(arr1), len(arr2), len(arr3)
        minLen = min(l, m, n)

        def binarySearch(target, array):
            left, right = 0, len(array)- 1
            while left <= right:
                middle = left + (right - left) // 2
                if target == array[middle]: return True
                elif target < array[middle]: right = middle -1
                else: left = middle + 1
            return False


        def search(loopingArray, array2, array3):
            result = []
            for num in loopingArray:
                if (binarySearch(num, array2) and (binarySearch(num, array3))):
                    result.append(num)
            
            return result
        
        if minLen == l: return search(arr1, arr2, arr3)
        elif minLen == m: return search(arr2, arr1, arr3)
        else: return search(arr3, arr1, arr2)








