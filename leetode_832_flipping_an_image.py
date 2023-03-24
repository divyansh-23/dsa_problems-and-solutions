'''
832. Flipping an Image
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].
 
Example 1:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:
Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 
Constraints:
n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.
'''

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        # Time: O(N), where N is the total number of elements in image
        # Space: O(1), where no additional space is used

        #Approach 1: First flipping it horizontally and then running a loop again to reverse

        for i in range(len(image)):
            left = 0
            right = len(image[i]) - 1
            while left <= right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                left += 1
                right -= 1
            for j in range(len(image)):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        return image                              

'''
        # Approach 2(Editorial): Flipping and inverting the values simultaneously using XOR operator. This is possible because the values in the matrix are only 0 and 1 and XOR with 1 (element ^ 1) inverts it.
        for row in image:
            for i in range((len(row) + 1)/2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^1
                # row[i], row[len(row) - 1 - i] = row[len(row) - 1 - i], row[i]
                # row[i], row[-i-1] = row[-i - 1], row[i]
        return image
'''




