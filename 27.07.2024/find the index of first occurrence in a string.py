class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        st=haystack
        s=needle
        for i in range(len(st)):
            if s[0]==st[i]:
                if s==st[i:len(s)]:
                    return i
            else:
                return -1
