class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = -1 
        n2 = -1
        c1 = 0
        c2 = 0
        for i in range(0,len(nums)):
            if nums[i] == n1:
                c1 += 1
            elif nums[i] == n2:
                c2 += 1
            elif c1 == 0:
                n1 = nums[i]
                c1 = 1
            elif c2 == 0:
                n2 = nums[i]
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        res = []
        c1 = 0 
        c2 = 0
        for i in range(len(nums)):
            if nums[i] == n1:
                c1 += 1
            elif nums[i] == n2:
                c2 += 1
        if c1 > len(nums) //3:
            res.append(n1)
        if c2 > len(nums)//3:
            res.append(n2)
        return res
