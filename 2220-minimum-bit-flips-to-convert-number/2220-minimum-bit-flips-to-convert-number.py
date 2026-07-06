class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = bin(start ^ goal).count('1')
        return answer