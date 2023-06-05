class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = min(strs,key = len)
        for i,ch in enumerate(res):
            for j in strs:
                if j[i] != ch:
                    return res[:i]
        return res
