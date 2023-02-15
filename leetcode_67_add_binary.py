'''Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        '''SOLUTION 1 - complexity O(n+m)

        return '{0:b}'.format(int(a, 2)+ int(b, 2))
        '''

        #Solution 2-- Time and Space both == O(max(N, M))
        
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = [ ]

        #loop running from the last index of the string i.e. 'n-1' to the first index i.e. 0 in reverse order
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            #this is to reset the carry to either 1 or 0
            carry //= 2

        
        #to handle last the edge case where the whole string is covered but there still remains a carry 1
        if carry == 1:
            answer.append('1')
        answer.reverse()

        return ''.join(answer)


        ''' solution 3: Bit Manipulation(solution without using + operator)
        #Time complexity = O(n+m), where n and m are lengths of the input strings a and b
        #Space = O(max(N, M)) to keep the answer



        x, y = int(a, 2),  int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        
        #because when converting x to binary its in the format '0b10001'
        return bin(x)[2:]
        
        '''
