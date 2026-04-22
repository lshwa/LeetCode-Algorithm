class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0

        for item in nums:
            if item % 3 != 0:
                answer += 1
        
        return answer
        