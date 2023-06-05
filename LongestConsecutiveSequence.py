class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = set(nums)
        longlen = 0
        for i in range(len(nums)):
            if nums[i]-1 in lst:
                continue 
            currlen = 1
            tmp = nums[i]
            while tmp+1 in lst:
                currlen += 1
                tmp += 1
            longlen = max(longlen,currlen)
        return longlen
