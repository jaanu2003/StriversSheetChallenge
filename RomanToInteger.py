class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I':1, 'V':5 , 'X':10 , 'L':50,'C':100,'D':500,'M':1000}
        res = 0
        v = 0
        for i in range(len(s)):
            p = a[s[i]]
            if p > v:
                res += p - 2*v 
            else:
                res += p 
            v = p 
        return res
