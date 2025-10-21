class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        ascii = []
        
        for ch in s:
            ascii.append(ord(ch))
        
        for i in range(len(ascii) - 1):
            score += abs(ascii[i] - ascii[i + 1])

        return score