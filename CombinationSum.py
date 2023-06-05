
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(s , target , ds:List[int]):
            if target < 0:
                 return 
            if target == 0:
                res.append(ds)
                return 
            for i in range(s,len(candidates)):
                    
                    solve(i,target-candidates[i],ds+[candidates[i]])
                    
        candidates.sort()
        solve(0,target,[])
        return res
