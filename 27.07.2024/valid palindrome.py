class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp=""
        for i in s:
            if i.isalnum():
                if i.isupper():
                    temp+=i.lower()
                else:
                    temp+=i
        if temp == temp[::-1]:
            return True
        else:
            return False
