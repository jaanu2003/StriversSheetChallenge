class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = [False]*n
        d1 = [False]*(2*n-1)
        d2 = [False]*(2*n-1)
        def solve(idx,ds):
            if idx == n:
                res.append(ds)
                return 
            for i in range(n):
                if col[i] or d1[idx+i] or d2[i - idx+n-1]:
                    continue 
                col[i] = d1[idx+i] = d2[i - idx + n - 1] = True
                solve(idx+1,ds+['.'*i+'Q'+'.'*(n-i-1)])
                col[i] = d1[idx+i] = d2[i-idx+n-1] = False
        solve(0,[])
        return res
