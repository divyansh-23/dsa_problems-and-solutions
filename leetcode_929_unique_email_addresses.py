'''
929. Unique Email Addresses

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
'''

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        '''
        #Approach 1: first attempt- brute

        output_email_set = set()

        def filter_and_add_email(email):
            split_by_attherate = email.split("@")
            local_name = split_by_attherate[0]
            domain_name = split_by_attherate[1]
            local_name_split_by_plus = local_name.split("+")
            local_name = local_name_split_by_plus[0]
            local_name = local_name.replace(".", "")
            output_email_set.add(local_name + "@" + domain_name)

        for x in emails:
            filter_and_add_email(x)
        
        return len(output_email_set)
        '''

        #Approach 2: Cleaner code using split and replace

        # Hash set to store all the unique emails
        outputEmail = set()
        for email in emails:
            # Split into two parts: local and domain
            localName, domainName = email.split("@")
            # Split local by '+' and replace all '.' with ''.
            localName = localName.split("+")[0].replace(".", "")
            # Concatenate local, '@', and domain.
            outputEmail.add(localName + "@" + domainName)
        
        return len(outputEmail)


        '''
        #Approach 3: Without using split and replace

        uniqueEmails = set()

        # Iterate over each character in email.
        for email in emails:
            cleanMail = []

            # Iterate over each character in email.
            for currChar in email:
                # Stop adding characters to localName.
                if currChar == '+' or currChar == '@':
                    break

                # Add this character if not '.'.
                if currChar != '.':
                    cleanMail.append(currChar)

            # Compute domain name (substring from end to '@').
            domainName = []
            for currChar in reversed(email):
                domainName.append(currChar)
                if currChar == '@':
                    break

            # Reverse domain name and append to local name.
            domainName = ''.join(domainName[::-1])
            cleanMail = ''.join(cleanMail)
            uniqueEmails.add(cleanMail + domainName)

        return len(uniqueEmails)
        '''



