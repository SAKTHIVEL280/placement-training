class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s) - 1
        temp = []
        for i in range(l,-1,-1):
            temp.append(s[i])
        for i in range(l+1):
            s[i] = temp[i]
