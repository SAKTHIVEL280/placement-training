class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=["(","[","{"]
        c=[")","]","}"]
        l=len(s)
        t=0
        if l%2!=0:
            return False
        else:
            for i in range(l):
                for j in range(3):
                    if s[i]==a[j]:
                        if s[i+1]==c[j]:
                            i+=1
                            t+=1
                        else:
                            return False
        if t==l/2:
            return True
