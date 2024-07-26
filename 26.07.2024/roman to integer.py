class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r= {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
        l=len(s)
        i = l-1
        limit = l-1
        t = 0
        while i>=0:   
            if i < limit and r[s[i]] < r[s[i+1]]:
                t-=r[s[i]]
            else :
                t+=r[s[i]]
            i-=1
        return t
