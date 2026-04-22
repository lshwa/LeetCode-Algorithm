class Solution:
    def maxDistinct(self, s: str) -> int:
        substring = set()

        for item in s:
            substring.add(item)
        
        return len(substring)
        