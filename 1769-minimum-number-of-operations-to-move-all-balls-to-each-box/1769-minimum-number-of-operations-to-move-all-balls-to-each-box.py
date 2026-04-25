class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = []

        for i in range(n):
            total = 0
            for j in range(n):
                if boxes[j] == "1":
                    total += abs(i - j)
            answer.append(total)
        return answer