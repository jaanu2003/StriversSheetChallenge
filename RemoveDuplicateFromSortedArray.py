class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        i = 0 
        j = 0
        nums[j] = nums[i]
        for i in range(1,len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j+1
       
