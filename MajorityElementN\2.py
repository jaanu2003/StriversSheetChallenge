class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        p = 0
        for  i in nums:
            if c == 0:
                p = i 
            if i == p :
                c += 1
            else:
                c -= 1
        return p
