class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispalin(s):
            return s == s[::-1]
        def solve(idx,s,ds,res):
            if(idx == len(s)):
                res.append(ds)
                return 
            for i in range(idx,len(s)):
                if(ispalin(s[idx:i+1])):
                    solve(i+1,s,ds+[s[idx:i+1]],res)
        solve(0,s,[],res)
        return res

    
        
