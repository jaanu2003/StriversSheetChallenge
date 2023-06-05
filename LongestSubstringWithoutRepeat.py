class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l = 0
        mx = 0 
        for r,c in enumerate(s):
            if c in m:
                l = max(l,m[c]+1)
            mx = max(mx,r-l+1)
            m[c] = r 
        return mx

      
