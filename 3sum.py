class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue 
            j = i+1
            n = len(nums)-1
            while j < n:
                s = nums[i]+nums[j]+nums[n]
                if s>0:
                    n -= 1
                elif s<0:
                    j += 1
                else:
                    lst.append([nums[i],nums[j],nums[n]])
                    j += 1
                    while nums[j-1] == nums[j] and j < n:
                        j += 1
        return lst
    

                    
