class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 100000
        prefix = ''

        #1. 제일 짧은 문자열 길이
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        
        #2. 문자 하나씩 비교
        for i in range(min_len):
            char = strs[0][i]

            for s in strs:
                if s[i] != char:
                    return prefix
            
            prefix += char
        
        return prefix