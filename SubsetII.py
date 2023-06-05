class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(s,sub):
            res.append(sub)
            if s == len(nums):
                return 
            for i in range(s,len(nums)):
                if i > s and nums[i] == nums[i-1]:
                    continue 
                solve(i+1,sub+[nums[i]])
        nums.sort()
        solve(0,[])
        return res
