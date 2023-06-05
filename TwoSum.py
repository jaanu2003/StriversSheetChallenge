class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          s = {}
          for i,j in enumerate(nums):
              a = target - j 
              if a in s:
                  return [s[a],i]
              s[j] = i
          return []
        
