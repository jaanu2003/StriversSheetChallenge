class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        i = 0
        while i < n:
            j = i+1
            while j < n:
                t1 = target - nums[i] - nums[j]
                left = j + 1
                right = n - 1

                while(left < right):
                    s = nums[left] + nums[right]
                    if(s < t1):
                        left += 1
                    elif(s > t1):
                        right -= 1
                    else:
                            lst = []
                            lst.append(nums[i])
                            lst.append(nums[j])
                            lst.append(nums[left])
                            lst.append(nums[right])
                            res.append(lst)
                            third = nums[left]
                            fourth = nums[right]
                            while left < right and nums[left] == third:
                                left += 1
                            while left <  right and nums[right] == fourth:
                                right -= 1
                t = nums[j]
                while j < n and nums[j] == t:
                    j += 1
            t2 = nums[i]
            while i < n and nums[i] == t2:
                i += 1
        return res 
            

                    
