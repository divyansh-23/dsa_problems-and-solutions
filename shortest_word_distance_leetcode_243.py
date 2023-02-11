'''Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 
Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1


Solution:- 
'''

class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        shortestDistance = len(wordsDict)
        idx1, idx2 = -1, -1
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                idx1 = i
            elif wordsDict[i] == word2:
                idx2 = i

            if idx2 > -1 and idx1 > -1:
                shortestDistance = min(shortestDistance, abs(idx1 - idx2))

        return shortestDistance

