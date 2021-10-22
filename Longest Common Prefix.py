class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        short = float('inf')
        for word in strs:
            short = min(short,len(word))
            
        for index in range(short):
            for i in range(1,len(strs)):
                if strs[i][index] != strs[i-1][index]:
                    return res
            res+=strs[0][index]
                
        return res
