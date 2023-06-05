class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        t = [False] * len(nums)
        def solve(ds):
            if(len(ds) == len(nums)):
                res.append(ds)
                return 
            for i in range(len(nums)):
                if t[i]:
                    continue 
                t[i] = True
                solve(ds + [nums[i]])
                t[i] = False
        solve([])
        return res

      
