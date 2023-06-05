class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        def solve(s,target,ds):
            if target < 0:
                return 
            if target == 0:
                res.append(ds)
                return 
            for i in range(s,len(candidates)):
                if i > s and candidates[i] == candidates[i-1]:
                    continue 
                solve(i+1,target-candidates[i],ds+[candidates[i]])
        candidates.sort()
        solve(0,target,[])
        return res
