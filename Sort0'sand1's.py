class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1
        
        for i in range(len(nums)):
                if nums[i] == 0:
                    nums[low],nums[mid] = nums[mid],nums[low]
                    low += 1
                    mid += 1
                    break
                elif nums[i] == 1:
                    mid += 1
                else:
                    nums[mid],nums[high] = nums[high],nums[mid]
                    high -= 1
                    break
        return nums
