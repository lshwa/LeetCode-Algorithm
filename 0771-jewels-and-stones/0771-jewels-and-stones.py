class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0

        for i in range(len(stones)):
            if stones[i] in jewels:
                answer += 1
        
        return answer