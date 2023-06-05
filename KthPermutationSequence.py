class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''
        nums = [i+1 for i in range(n)]
        fact = [1]*(n+1)
        for i in range(2,n+1):
            fact[i] = fact[i-1]*i
        k -= 1
        for i in range(n-1,-1,-1):
            j = k//fact[i]
            k %= fact[i]
            res += str(nums[j])
            nums.pop(j)
        return res

