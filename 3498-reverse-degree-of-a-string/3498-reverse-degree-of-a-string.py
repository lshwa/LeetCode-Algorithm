class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0

        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))
            answer += value * (i + 1)

        return answer

        