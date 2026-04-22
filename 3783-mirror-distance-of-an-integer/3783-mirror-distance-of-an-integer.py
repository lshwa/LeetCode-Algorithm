class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = str(n)
        temp = int(temp[::-1])

        return abs(n - temp)
        
        