class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        return sum(int(d) * s.count(d) for d in set(s))