class Solution:
    def minPartitions(self, n: str) -> int:
        answer = 0

        for i in range(len(n)):
            if answer < int(n[i]):
                answer = int(n[i])
        
        return answer